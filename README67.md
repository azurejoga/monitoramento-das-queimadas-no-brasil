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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9018312d-6617-32e6-afab-cef613ff289e | 3.00536 | -51.4469 | 2025-09-14 05:25:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| baa7e539-9be4-3dee-a8a5-10389f6a9eb3 | -3.22955 | -47.63458 | 2025-09-14 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a790faf-4cf1-3660-9dc9-8d9a1b40bbf5 | -3.22239 | -47.63365 | 2025-09-14 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df4f3586-c32d-3183-88a6-05ac363c163b | -6.80644 | -51.37688 | 2025-09-14 05:27:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 855ffad6-e6c6-389b-b249-fdb63edc0b8f | -1.23788 | -54.10489 | 2025-09-14 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e33c9ecf-5ff5-3b63-8697-0dca322cdf93 | -4.48905 | -48.11233 | 2025-09-14 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8bb6029-ac82-3fdf-8615-77eeef016985 | -4.28203 | -56.3319 | 2025-09-14 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b962c31a-dbf3-3ba9-aa1b-d9bd4bdb8323 | -1.58895 | -55.85443 | 2025-09-14 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcb85c67-691d-37f7-b228-be7139a0a467 | -3.73393 | -55.94697 | 2025-09-14 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d0c9e44-761a-37fb-8136-a973614efb8a | -7.71274 | -55.45217 | 2025-09-14 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d02e083-b811-3907-9361-7f8f90188f08 | -1.22479 | -54.1253 | 2025-09-14 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68f1193e-4d6d-381f-b558-b3c856dba810 | -3.73452 | -55.9431 | 2025-09-14 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db4f7ba7-e117-3d05-a3e0-3af964b6f6b7 | -7.71206 | -55.45691 | 2025-09-14 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d48c389-5a73-3588-9620-0e240a158b5e | -1.22939 | -54.12575 | 2025-09-14 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a663255-ee38-380c-ac55-e3a077d6a352 | -4.48812 | -48.11909 | 2025-09-14 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2659fefd-e5bc-35a0-8a3c-1b4b68425495 | -1.23765 | -54.1031 | 2025-09-14 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21a19f4d-0614-3c72-a256-d907b5db3f1b | -4.48355 | -48.11715 | 2025-09-14 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3ebe8d7-ef04-351c-97f6-f1595c647fe7 | -12.67435 | -61.19021 | 2025-09-14 05:29:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 632595ac-bd34-3fa6-8f3d-73bb6c1c07ef | -12.6614 | -54.6673 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a8179db-a39c-3c2d-b096-456526ad077d | -12.93441 | -54.74168 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d36fb708-6af2-371f-949e-8930fb5647be | -12.6975 | -54.67506 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8790083-997f-3313-9ea3-c968f7898214 | -15.20248 | -52.49121 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3394ce67-f672-36d0-9c4e-b33ea3524523 | -12.68347 | -54.70314 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b7cdf05c-400e-3bfb-b610-c9a27d6fe2a2 | -12.6971 | -54.67831 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 22c082ab-19ea-3212-b2ef-f8f4678b4e16 | -11.16113 | -57.18348 | 2025-09-14 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceffe9af-6d3f-3ab9-abd9-02ce8a67d27c | -12.67907 | -54.69591 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad8455f5-4920-37e8-9220-c1ce604bc067 | -15.14853 | -52.4761 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93f6277f-93fa-3288-9af5-f4bfa2af79c7 | -14.17814 | -54.06236 | 2025-09-14 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71a3b0d3-c6ae-39a8-8da2-ce127884c7f9 | -12.45253 | -57.78878 | 2025-09-14 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8d6bd6f-22ac-37c2-92bb-4caf051f9943 | -11.47316 | -50.76073 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f8902fdb-ee8b-3c7b-b5a7-6942db8eb71c | -11.27331 | -51.1131 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 115fd1de-1752-3eac-936e-aa4bff793925 | -10.22884 | -67.34766 | 2025-09-14 05:29:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ff40518-efe7-351b-9484-c0bef1735488 | -12.69152 | -54.72345 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c4d5fdc-104d-358e-8411-5bcfc4de50b2 | -12.67182 | -54.66865 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 020e8103-8989-38c4-a74e-3dceb77c45fa | -12.70313 | -54.71493 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4f051f92-76dd-3a9a-a66c-fe302cedac66 | -12.68907 | -54.70052 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| cc6cb646-2960-3719-99e5-1ad915acdede | -12.91799 | -54.74624 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9ce9e4be-00d5-3e46-9783-6aca5f1dcaa8 | -12.65552 | -54.66625 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f321133-5611-3e4b-92d6-d34311ee5e6a | -12.86478 | -62.13551 | 2025-09-14 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ea26873-dd1f-3e09-bb2b-f0d57300f315 | -15.15433 | -52.47232 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1ec52811-5481-3a8e-869d-f7a47d6e4ff4 | -12.92399 | -54.74047 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 55d1c2d0-9df7-30a2-9efd-19709e085a48 | -12.67586 | -54.67893 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e236bccd-3d39-3fe4-b866-74ffe5489c91 | -12.66503 | -54.68102 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a5e55200-a78c-3828-a897-1f044ad025b9 | -12.69229 | -54.67444 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8677821e-34d4-38b0-99cd-b9bc0da654dd | -12.67143 | -54.67189 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e85bb47-1aaa-3f6f-8ebd-dba3ff6c260d | -12.8676 | -62.13972 | 2025-09-14 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ca46558b-c25a-3792-b07e-22cb18c09591 | -12.65822 | -54.68639 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e932c63-7c6f-33e3-922b-aba8dd56ac2b | -12.68427 | -54.69659 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 19516544-2711-36e7-92f3-e9213e12d20e | -12.69269 | -54.67118 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2aea7850-6910-3adc-935c-aef23c5ff29a | -12.68988 | -54.69398 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 29f2309f-2d7e-3e0d-baae-870aabef1579 | -12.66345 | -54.69406 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 246d70fe-f359-3cd1-9c6f-986ed9703f4d | -15.10834 | -52.49988 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9316e2c9-c1dc-33ac-8358-22105b1ea66f | -11.47184 | -50.77211 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 59de16b7-5649-3b9c-977e-3a1699f7b002 | -12.70392 | -54.70857 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f2e82f56-1bab-3441-9644-e46b3c60de78 | -12.70031 | -54.69513 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 88f92385-1a28-3fb5-a87a-3a26102e536f | -12.70353 | -54.71174 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc2c1071-3c2d-336a-9cc0-0b7ce5c67db3 | -12.68068 | -54.6828 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| a4f5dcce-1294-3d86-9cb4-525a375ab1f5 | -12.32684 | -64.08235 | 2025-09-14 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e69a496d-5e82-3876-acbe-13160f15d75b | -12.69713 | -54.7208 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 74bab1c4-ac8c-3ce4-ad29-3a47dc78dec6 | -12.67626 | -54.6757 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7f8196de-1bc8-3f7e-b98e-c76f6adaa86b | -12.68548 | -54.68679 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| b5219755-070b-3cb8-9f44-fa5cf5538b8d | -12.6603 | -54.6702 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7dc2afc-932b-32ec-b038-5cb59baa41a3 | -12.69068 | -54.68745 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 89fa6eca-a631-3c28-b646-5383d24a3e35 | -12.65864 | -54.68316 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4e471414-3169-3c60-95e7-baaead5a7737 | -11.28682 | -51.10929 | 2025-09-14 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d5c38846-aaf5-3b54-b2a2-0353e3fd460d | -12.69188 | -54.67769 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 3b3fa952-2db7-3ad8-b27a-b8c60a7e6ba8 | -12.70352 | -54.66921 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38ca4d90-8755-3e6c-8cd0-9ae2988fa0f6 | -12.67704 | -54.66925 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 01e4d074-4561-37c6-8db3-38eb6f9c061f | -12.6995 | -54.70164 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c8d1a4d6-1ebb-3b60-9e5a-eadb7c1fd684 | -12.87325 | -62.17071 | 2025-09-14 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bca7ea8b-791a-31b2-a7c9-21886f4b69c6 | -12.45734 | -57.78845 | 2025-09-14 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13842089-f7b3-346f-8be7-b33e4f387ebb | -12.67546 | -54.68218 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| c76490f5-3e1c-3e6b-8e08-946034a12356 | -14.61941 | -52.02721 | 2025-09-14 05:29:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d58a7054-5761-37fc-b3fd-3110b9032b1d | -12.70512 | -54.69894 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3955fe8-5c73-3796-b1e2-7626d024cf36 | -11.3971 | -50.44978 | 2025-09-14 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e7e21900-9d2e-331a-9a38-0a1e5deb8c0c | -10.23051 | -67.35026 | 2025-09-14 05:29:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b0ee4eb-58c0-301b-bdfa-c407dc817294 | -12.67665 | -54.67248 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6a2441fc-6386-3240-b4ff-be7ed4f464fa | -12.67948 | -54.69262 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 100ed2db-6389-344d-b6e8-74ff3ae85e90 | -12.67787 | -54.70576 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7244a64-a991-3c5d-adea-134c81918a12 | -9.12051 | -67.49007 | 2025-09-14 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e19fb52-0210-333e-83e6-ac61e79e0f5a | -11.44193 | -50.47319 | 2025-09-14 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95a87e59-090a-377e-94f8-69e000ab55b0 | -12.6562 | -54.6666 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7671122-be7e-3297-9515-7348792efd39 | -12.67507 | -54.68544 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 5c90ed70-ec97-3770-9343-ef8c84d3ca97 | -11.36885 | -59.14141 | 2025-09-14 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e3f9ebc-e660-371b-bc9e-c2839382e3d1 | -12.66621 | -54.67125 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 399d2bdb-d9a3-3b4a-bb23-481a9a7d9cc0 | -12.86534 | -62.13183 | 2025-09-14 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93739858-3634-3c62-84b4-b01b261107e7 | -12.66945 | -54.68813 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c3b80734-3294-3d05-b16f-a62b2ccc6379 | -12.6991 | -54.70487 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 313ec21b-7e61-38da-8181-7bdff53f29fb | -12.68226 | -54.66987 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 127a9cf4-1c5d-3303-a743-28510479a2f1 | -12.65905 | -54.67993 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 482f38d7-95de-3001-8f9a-a51541815d5f | -12.88503 | -62.1161 | 2025-09-14 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dea4554-99bd-36e2-b93b-0ca7f6ebed65 | -12.70071 | -54.69189 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f162b57b-2ad9-3e59-a11f-8f2237293094 | -12.67386 | -54.69529 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5809c979-7e94-3cce-871e-eebf7097a8b2 | -12.70152 | -54.68538 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 3eb8ebde-d2a6-38ce-ae61-0215d5ad3b34 | -14.7224 | -55.66002 | 2025-09-14 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c8ab7c89-981f-3bcd-8006-0ad0238c35c9 | -12.69509 | -54.69457 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 67acaa54-d87a-305b-9b2f-29d92cad1d93 | -11.40994 | -55.36045 | 2025-09-14 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f88af6cb-5531-3f7d-9d52-c2a1c46dff45 | -12.65989 | -54.67345 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14c2e713-168f-30a2-9ee1-2eb748572470 | -12.67747 | -54.709 | 2025-09-14 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 892e6a91-6728-300f-a2b9-431379d02444 | -15.15525 | -52.4721 | 2025-09-14 05:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README68.md)
