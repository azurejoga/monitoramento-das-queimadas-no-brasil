# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 880c54a7-51d9-3430-8407-1f6d8c0c65cb | -12.92359 | -54.7437 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5e456b68-9fee-3312-9814-3bc38dac92dd | -11.36818 | -59.14606 | 2025-09-14 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9cd8638-caa8-33b5-b8cc-f4af512b1171 | -12.68667 | -54.67704 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 1b96b444-b392-32b2-ae03-6bb777abc29a | -11.28908 | -51.10121 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dc922db1-21b4-32d0-b5d3-64cc4f0d12a3 | -11.28846 | -51.10656 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fdce6a0-7535-3edf-b307-0718da3e6211 | -11.47119 | -50.77777 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b38ff4d2-a29a-3ea1-b97b-b13a1cf691a9 | -12.92319 | -54.74691 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e22744d3-845d-3eb7-8ee9-79188e890065 | -12.67783 | -54.66277 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 641c4367-e085-3693-8e0e-ba5900b091e4 | -12.70273 | -54.71813 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9be89b92-5dc1-3e54-a817-daa419d3ab0c | -12.69108 | -54.6842 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| b3480983-c251-343e-a00d-1cd43ad92a2d | -12.69752 | -54.7176 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9ba8ea90-26d4-3cd3-acda-baf11906b482 | -12.68789 | -54.71015 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa21866d-9028-34e7-9539-4f7f3cf23555 | -11.44501 | -50.47421 | 2025-09-14 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d05dac07-1ce5-3267-b4fb-3d1879de06f0 | -6.94199 | -71.50181 | 2025-09-14 05:29:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ef7ad6f-7bd9-3823-a236-e714b22dd3b9 | -12.67025 | -54.68161 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d12c7696-82e1-364d-9270-1e53a03e3084 | -12.68387 | -54.69987 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 858892f3-017f-3bbc-9748-b75132681585 | -9.12094 | -67.49303 | 2025-09-14 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dcbb523-3aa2-31c7-9815-0f288bb148e1 | -12.69673 | -54.72397 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87effb47-b7c6-3d31-8b36-75e74aa1cee0 | -12.69028 | -54.69072 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cf8ad485-9e97-39ff-bde5-f7dc0ed73392 | -12.6551 | -54.66949 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebbe2953-d4ec-320f-8cd4-a39ea6a228a7 | -12.65943 | -54.68356 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 12ffda8e-9078-315b-81a8-160f2439997f | -12.68588 | -54.68354 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6084a62a-7ef2-3423-8369-5b2a3e16c93c | -12.93481 | -54.73851 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dc05422e-fb2b-3833-ad84-d96f771a2d80 | -12.32352 | -64.08179 | 2025-09-14 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0419785-f06b-30a1-bbe3-6a1b2e117bc4 | -12.66464 | -54.68427 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 72578486-7a9a-3029-908c-f5b760dee283 | -12.67867 | -54.6992 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 891b3b1c-7438-3a30-a9f8-0bbe5cb86b1d | -12.70953 | -54.70594 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b88c9d8a-99f6-3dce-bf83-682b40d75b71 | -12.70312 | -54.67244 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9254548f-d73d-3eca-b8e4-45fa9ce8cedd | -12.69309 | -54.66791 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f356fbc-dee9-39d0-b4aa-3fbdde1ea375 | -12.68147 | -54.67633 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4d3726f9-286a-31c9-ab1e-9965afc66343 | -11.01289 | -51.25108 | 2025-09-14 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 169cee9b-c9ad-3cae-b41c-0d497f5e4628 | -14.17856 | -54.05874 | 2025-09-14 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07121c43-dc4a-3dd4-b865-2fb166b6d2c5 | -6.94259 | -71.49845 | 2025-09-14 05:29:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08ddc0d5-6a6f-33bb-9ed5-32ff8705ece5 | -12.88165 | -62.11557 | 2025-09-14 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e9c5362-b3ff-37cc-b215-170fdb40caba | -12.68467 | -54.69332 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4bbbc287-6300-35e7-98a7-b2b81e01e7b5 | -12.65983 | -54.68032 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 19ae7d6d-760e-32c7-b3bb-1f033cf0e5da | -12.66985 | -54.68487 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 308f36f2-6bdd-34f2-a2cd-259c76306f55 | -12.3202 | -64.08125 | 2025-09-14 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cff1ffd-35a7-3fe4-9a11-f5519e31a162 | -12.68108 | -54.67955 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 241ffb12-a58e-3451-a7d6-d43c815ada3a | -12.66905 | -54.69141 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 398fc26a-bf79-3b3f-a06d-0d489dc39954 | -12.65904 | -54.6868 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 05ca2ebf-8e7b-3c9f-81a5-13df75bcbc31 | -12.66022 | -54.67708 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 484fb3c4-18c0-3504-9931-844e65ff1c8a | -12.67222 | -54.6654 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90639482-372a-3bde-9f5d-3917958c3501 | -12.67427 | -54.69201 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b8cc9c6-7177-38b4-87eb-4901bd45c775 | -12.66114 | -54.66367 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be28afe8-c6bf-3a12-b558-842d4ee0b00f | -12.68186 | -54.67311 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 403f1318-a6d8-34bc-afb8-a01988ad023c | -15.11453 | -52.5005 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5885e02-57d2-3421-8185-a33803d1fddf | -13.18052 | -55.62337 | 2025-09-14 05:29:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 690d6979-2f3c-39f5-89a9-05367439cec3 | -12.69191 | -54.72027 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ea34c532-2268-3721-82d7-0a452890c646 | -12.66384 | -54.69079 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2e4df0b0-de66-3c83-9e2e-3c4a159ee95c | -11.27498 | -51.11034 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7b1ad48f-d8ee-3b98-b268-b68bb9ab8a12 | -15.08604 | -52.47435 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b098746-e47b-31de-96f6-293525c12166 | -12.6983 | -54.66856 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00dee1a4-eac1-3ef0-b4c5-d90376dcfe62 | -12.68747 | -54.67052 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| deb430ea-4112-37c6-8b8c-ffa593ff825a | -11.29117 | -51.13965 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01d9b846-a35f-3f80-ad73-39108265a346 | -12.68266 | -54.66663 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 77e17d6d-ff58-331f-b736-5991944aa0cf | -12.67827 | -54.7025 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be581c82-4ce2-35e8-add9-86136117586a | -12.69231 | -54.71707 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 849e51a3-9038-3ac0-a154-72d22b7465f3 | -12.67306 | -54.70187 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d082719-7617-3505-abda-ff875a019c5b | -12.70192 | -54.68215 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 55262bb6-73e2-38e1-be61-08a2a1740bd9 | -12.66543 | -54.67776 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ddd7eb3-1421-3fd1-bfc3-764d79a956f2 | -12.09244 | -51.38335 | 2025-09-14 05:29:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7c6451c-137e-396f-845a-625be51ac706 | -11.47777 | -50.77856 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2c1230b2-fbfe-3db3-960a-1f9a6c834a3b | -15.91161 | -49.97606 | 2025-09-14 05:31:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 506ad087-25db-3a6f-b730-e7a1a433a5c2 | -22.66666 | -53.12628 | 2025-09-14 05:31:00 | NOAA-20 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ab493c2a-e775-36af-907d-2a60e3a3bb38 | -15.77139 | -53.47875 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de2fe924-99fc-32fd-bee5-50d52cf1cfac | -22.66068 | -53.12003 | 2025-09-14 05:31:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e5bcef2d-6519-3574-849c-ca4f41aa468b | -20.77143 | -56.94012 | 2025-09-14 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 47793209-8b68-3316-82b8-a9e4eface8c4 | -20.09821 | -54.60944 | 2025-09-14 05:31:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 287aac29-b500-37bd-84ad-c439047ddfde | -17.36194 | -52.90615 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2083c33d-2f57-35d6-a22e-f89db0227422 | -15.7817 | -53.48274 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bad77207-30cc-3a9e-93d7-e49eca21e8f8 | -16.36316 | -51.77175 | 2025-09-14 05:31:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ed5f72f-7d06-302b-ac6a-852635819501 | -16.71606 | -54.96406 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b56b7dc-6a44-3063-886c-67b77128c4b6 | -16.49636 | -55.12336 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 85fa58d0-7692-3de5-857a-a02c5d6008df | -15.59972 | -54.78167 | 2025-09-14 05:31:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3d7a8d7-dc66-3b5c-8738-6f84980ae660 | -15.26701 | -56.02808 | 2025-09-14 05:31:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6325f968-d291-3050-a54f-27548f29afdd | -15.76375 | -53.48424 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ceb7c562-f78d-3a00-be76-e521287dd2e7 | -20.26623 | -57.16317 | 2025-09-14 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7b29666-bfa2-3f27-8df2-57e9942fe7ab | -17.82935 | -50.43069 | 2025-09-14 05:31:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ad4d71c-0435-3226-a85c-a871e29fe5af | -20.56303 | -54.59282 | 2025-09-14 05:31:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9a79721-68df-34b5-a211-ef2216ff1a6d | -15.60553 | -54.77864 | 2025-09-14 05:31:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6c65f98-f81e-3748-ae70-db8a526cc2c6 | -16.25148 | -56.63148 | 2025-09-14 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5c765a7b-0cec-38b5-932e-01e8c6f61d14 | -22.52679 | -52.99829 | 2025-09-14 05:31:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 1eab913c-e8b3-3f55-95c4-a111cc31c2fc | -15.80124 | -52.2035 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b26517ad-4d46-3d63-b78c-c616b74a2d34 | -15.93354 | -49.97568 | 2025-09-14 05:31:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ab24a0b9-a113-3d4a-aff1-58baab7ec361 | -16.36204 | -51.77227 | 2025-09-14 05:31:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2263ede-8bc4-3ae0-9e41-7e2337638552 | -22.52662 | -52.99882 | 2025-09-14 05:31:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 47bb1512-6d0d-3a07-b9fe-8ccb3a0cc332 | -15.93595 | -49.97071 | 2025-09-14 05:31:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4f7e904b-f55e-3790-8a15-3008f5b0a54f | -15.59432 | -54.78124 | 2025-09-14 05:31:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6f1744e-f26a-331d-b8fb-a32882a486fc | -16.35548 | -51.77167 | 2025-09-14 05:31:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b555cd8-6072-3b5a-b1bb-057fb6162a09 | -16.49102 | -55.12294 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bb00b5fd-74c7-38dd-a141-8feda36852aa | -16.50248 | -55.16421 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 205a7e05-94d1-3cea-aec1-2b0f76052b06 | -16.356 | -51.76617 | 2025-09-14 05:31:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f33feabc-2b74-31d7-aa98-e29a1b5066ba | -15.91894 | -49.97576 | 2025-09-14 05:31:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 410ca8ce-aa0f-3515-9dcb-9c8a7777de47 | -15.80498 | -52.20216 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ef141f6-fb06-3fc9-aac9-90f8f3caf4d3 | -16.49142 | -55.11941 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 608279d9-05d3-3afb-bac9-391e00373b96 | -17.79685 | -51.72723 | 2025-09-14 05:31:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b46bdba1-9787-3b35-8557-f784c85c74fb | -20.84217 | -56.89694 | 2025-09-14 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd4720f4-5f2f-3688-9bca-5d8df8abf7ae | -15.76297 | -52.23584 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a02f4d08-3ede-3067-afe1-279a3ade71f9 | -15.91337 | -49.97838 | 2025-09-14 05:31:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |


[Clique aqui para ver as próximas entradas](README70.md)
