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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94f39c67-e655-3980-9ca2-84420d042e7b | -4.49456 | -42.55495 | 2026-08-14 00:11:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 578.8 |
| af2b824d-d170-3de6-b29f-a157481bfdfd | -8.604 | -54.6739 | 2026-08-14 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 5ab0c583-b3b8-3828-9627-aac2d2c173cb | -2.64107 | -47.98446 | 2026-08-14 00:11:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 34f97302-517a-3246-989a-38c0c7b5cb96 | -9.98169 | -53.94976 | 2026-08-14 00:11:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| bd56fac4-435c-3429-b60e-e5b95dc9742e | -4.26987 | -49.36398 | 2026-08-14 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cd6b5c31-4ef4-3b80-aec6-0b964acfa70f | -9.13235 | -46.39986 | 2026-08-14 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 8ef6a1d7-5b33-381f-8d9e-14a377638311 | -9.98256 | -53.95594 | 2026-08-14 00:11:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 12959313-3c77-3925-880a-17c3fdcc5f9a | -3.84631 | -49.04131 | 2026-08-14 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 95f9c577-8b4d-3083-bec7-ec2c191fa77d | -6.10802 | -44.02713 | 2026-08-14 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 2cdab790-8392-3ad5-a65a-26ff7726d831 | -7.59837 | -46.46955 | 2026-08-14 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| a0de3bde-e6e1-3f6c-bf3b-a495d1341b38 | -9.49687 | -51.62748 | 2026-08-14 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c94b702d-dcaf-34d4-a4cb-d69cb49498de | -9.98316 | -53.9615 | 2026-08-14 00:11:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 04c22b88-49ef-3147-9b1a-7064621eb761 | -8.01766 | -55.12099 | 2026-08-14 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6f352218-4fa0-3b45-9198-ea290cdf8cce | -3.65718 | -55.54851 | 2026-08-14 00:11:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3eec715c-00d1-3ccc-bb13-295275d7a231 | -3.66331 | -48.97964 | 2026-08-14 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4fe65ae5-0689-35c3-9884-00378b9f3446 | -8.88882 | -60.56526 | 2026-08-14 00:11:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 6c7fc03d-cbe6-3224-b754-f9b775fce87e | -6.61523 | -59.03996 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 21bed374-1f3a-3893-80e6-4682b0306957 | -7.60939 | -46.46783 | 2026-08-14 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 66c38506-ac46-3221-a7d0-f8f256497604 | -6.84036 | -56.42281 | 2026-08-14 00:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| d6ca4b82-90c8-3528-aac0-9f76990d4da7 | -7.71292 | -46.23709 | 2026-08-14 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| bdb63c5a-03f3-3dd0-809b-2ed5d51f58c3 | -6.71234 | -58.93885 | 2026-08-14 00:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| d76efedf-52d7-3a6e-80f2-5fa733d4c8bb | -2.97943 | -51.68471 | 2026-08-14 00:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5bde2d98-af52-3262-b450-f103b7e10d3b | -7.71238 | -46.23155 | 2026-08-14 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a2da2fe7-88c0-393a-bcd1-e66a9d8c0c35 | -8.60785 | -54.67968 | 2026-08-14 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b433c751-0e32-34de-a506-209f7d1de7c3 | -6.61103 | -56.33658 | 2026-08-14 00:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6137ef73-b925-3f56-808d-b034ea2738d9 | -6.60187 | -56.34424 | 2026-08-14 00:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| baba34bb-4ecc-321e-b44b-529306b9a39d | -9.48738 | -51.63508 | 2026-08-14 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 23bfcbc0-c8a7-33ef-a79a-3b5bfa5ee646 | -4.00936 | -48.96114 | 2026-08-14 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| df46ac85-c056-352f-b14f-95e16de22727 | -9.59251 | -49.32497 | 2026-08-14 00:11:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b3931c62-ede7-3e83-9faf-11cf76dd16e9 | -8.55503 | -54.59782 | 2026-08-14 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c8731491-cd07-3dbe-a8b1-60a1c4297ebf | -4.49794 | -42.5137 | 2026-08-14 00:11:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| faaa0c08-4093-3c00-9065-37e7574e6eb1 | -1.49877 | -55.84815 | 2026-08-14 00:13:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3d4be7d2-5b35-38c2-a28e-68688b84aa9f | -3.24709 | -60.12846 | 2026-08-14 00:13:00 | TERRA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 12484749-5e13-3d8b-8990-a31cfd5fdfae | -1.83438 | -54.49205 | 2026-08-14 00:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 41ba5f27-883f-3016-9644-dd1f712e2204 | -1.82639 | -54.50331 | 2026-08-14 00:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1ca957be-cf8a-3a32-ac45-df70c65ed604 | 1.30818 | -50.68507 | 2026-08-14 00:13:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 3900a481-170e-3be3-b00f-b574246d9d30 | -3.24739 | -60.12177 | 2026-08-14 00:13:00 | TERRA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4e1e5b6e-1d01-3334-9fc3-1d50ef1c01be | -1.78295 | -55.52966 | 2026-08-14 00:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c075fb4a-1f40-3ad6-ad12-74a29544cef7 | -1.83576 | -54.50203 | 2026-08-14 00:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6e630ecb-6129-3a72-b46e-563980d3aa14 | -1.82777 | -54.51331 | 2026-08-14 00:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 255cf2fe-83c7-378b-bf06-37a3adef9344 | -4.49 | -42.53 | 2026-08-14 00:15:00 | MSG-03 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4d492678-a70c-392a-9d94-d4bc49b271c2 | -4.49 | -42.57 | 2026-08-14 00:15:00 | MSG-03 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1dff402c-2273-370e-ae8f-5a62ee36cccb | -4.52 | -42.53 | 2026-08-14 00:15:00 | MSG-03 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4e3b688e-a83b-3dab-bc60-af8c8c5d5145 | -21.9049 | -55.3755 | 2026-08-14 00:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 3d1342a3-d122-3e40-8908-a4ee5b7164dc | -6.6194 | -59.0609 | 2026-08-14 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 8148a137-bf2e-361a-9ded-6d15db430ca4 | -14.4734 | -45.6914 | 2026-08-14 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 60031bda-425b-3994-9561-e4028cb749b5 | -7.7123 | -46.2307 | 2026-08-14 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| ba3ac990-6271-3ca4-9d8a-bb33daf331f4 | -20.0293 | -48.0148 | 2026-08-14 00:20:00 | GOES-19 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 114.3 |
| b2a35a4d-22ab-3c35-a663-99c7685df5b1 | -20.0497 | -48.0102 | 2026-08-14 00:20:00 | GOES-19 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 8c0fdace-c310-355c-b471-417b886584cf | -4.5242 | -42.5549 | 2026-08-14 00:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 335.6 |
| dde6a552-f07e-3e2a-916f-51466d827975 | -4.5055 | -42.5561 | 2026-08-14 00:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1365.8 |
| deecc0e8-4515-3e8b-9506-5dd7f4fff09d | -4.5053 | -42.5796 | 2026-08-14 00:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d67d0f8d-d62c-3207-ab20-518d2e10a4bf | -9.9894 | -53.9608 | 2026-08-14 00:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8efbba0a-b2bd-3a5d-a89b-1e0041ef828d | -20.0299 | -47.9915 | 2026-08-14 00:20:00 | GOES-19 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e8cbd734-e8c1-3625-8c84-894634e0c921 | -4.4869 | -42.5336 | 2026-08-14 00:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 220.0 |
| 3054e8a3-5051-30b0-b070-d999a9e1e6a5 | -4.4868 | -42.5572 | 2026-08-14 00:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 245.9 |
| 85fd4d89-5438-3ce3-8d23-fb2ec1cc4c7b | -21.8843 | -55.379 | 2026-08-14 00:20:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 23fb8cb5-7d62-32a1-9909-389bb907eac2 | -14.4739 | -45.6682 | 2026-08-14 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| ec283003-8f6c-391e-ac22-fa1e2591b788 | -6.6195 | -59.0416 | 2026-08-14 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 8ea25464-a0f6-3b21-a753-826fdca86c36 | -11.4885 | -54.6273 | 2026-08-14 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 49a1450e-a5a2-36a5-83c0-ed90d626cb72 | -4.5244 | -42.5313 | 2026-08-14 00:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 331.2 |
| ba45aeeb-b84d-3e17-baa1-b8544093b58e | -11.4887 | -54.6068 | 2026-08-14 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8dd68b50-9a45-3b9a-bfba-946c11f3cbcd | -6.9145 | -43.6351 | 2026-08-14 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 53aee018-31b9-35ed-a28d-59792227ba0d | -11.5074 | -54.6256 | 2026-08-14 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| bc8b0ed7-9687-3eb5-b46c-289bc9621589 | -21.9054 | -55.3538 | 2026-08-14 00:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 169.6 |
| ab9c0810-8f1d-34a0-b115-b4b46692e552 | -4.5057 | -42.5325 | 2026-08-14 00:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1240.0 |
| 1e1ceecf-55b7-33aa-b24d-38442fedfd28 | -11.5076 | -54.6051 | 2026-08-14 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 73790715-ca8e-3829-8147-702339dc2d7f | -11.5076 | -54.6051 | 2026-08-14 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| bb69ee64-e077-3d66-ac51-b37c0963d15b | -4.4868 | -42.5572 | 2026-08-14 00:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 196.0 |
| 0188d5fe-bf20-35e8-8066-6dd237b88d2f | -21.8843 | -55.379 | 2026-08-14 00:30:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 5282ddea-1fe2-32c6-aedf-aee982b0b53b | -4.4869 | -42.5336 | 2026-08-14 00:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 193.8 |
| bf7ba92e-3892-3c3f-b5e7-386b5bdbbc32 | -11.4887 | -54.6068 | 2026-08-14 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a4b45e5c-cc7e-3e2c-9e4b-ede303904014 | -6.6194 | -59.0609 | 2026-08-14 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 26053a20-01d5-356d-9529-a551893b829b | -21.9049 | -55.3755 | 2026-08-14 00:30:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 164.6 |
| c6eb8847-195f-310d-b492-ddd3e1fcd824 | -4.5244 | -42.5313 | 2026-08-14 00:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 242.5 |
| 0c597f2e-1439-3c83-84de-2da761dcebd2 | -11.5074 | -54.6256 | 2026-08-14 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 47a12792-f71c-3f8a-887e-90ab05eb1677 | -11.4885 | -54.6273 | 2026-08-14 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 6a7aaa86-22ff-3624-b28e-6d6d9be6e748 | -6.6195 | -59.0416 | 2026-08-14 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.0 |
| e2e09ae7-cf8f-36e9-85c4-401d8b075bcb | -21.9054 | -55.3538 | 2026-08-14 00:30:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 65c05347-45e5-3ae1-90f8-1382737bc1d5 | -4.5057 | -42.5325 | 2026-08-14 00:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 773.8 |
| 0fec4f0f-1ed5-387d-b6bd-b1c8008005e0 | -6.9145 | -43.6351 | 2026-08-14 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| f6706265-d4b0-3bc2-ab91-36db02d8fce3 | -4.5242 | -42.5549 | 2026-08-14 00:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 225.7 |
| 2c214be9-76ba-3fc8-a9ec-e8e104ae51ad | -14.4734 | -45.6914 | 2026-08-14 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f54b6357-fc12-3739-9415-fd9df76a844a | -14.4739 | -45.6682 | 2026-08-14 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| cff3e54b-1d6c-3cc4-b43d-ee88c9a1d5f0 | -14.4539 | -45.6948 | 2026-08-14 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 98262b99-97b6-37dc-9c68-532f608a55ff | -4.5055 | -42.5561 | 2026-08-14 00:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 739.5 |
| e754de3d-69e5-3ba5-a3f5-1fe7d3032e4f | -21.9054 | -55.3538 | 2026-08-14 00:40:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 02114dde-ba9f-364c-b5a0-fb68c7817347 | -4.5244 | -42.5313 | 2026-08-14 00:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 141.9 |
| 69c5192d-4cf0-3600-a0b5-f70c5a185d5b | -4.5242 | -42.5549 | 2026-08-14 00:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 136.6 |
| 544845b0-cbed-35dd-8ab1-b0643528efbe | -4.4869 | -42.5336 | 2026-08-14 00:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 156.2 |
| 6822c47e-aaa8-3cbd-bd94-3c93f7c20dfd | -11.5076 | -54.6051 | 2026-08-14 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0a3df19a-bbc9-39cf-99e7-cd4b64f1415a | -15.112 | -48.6459 | 2026-08-14 00:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 47d50b84-d437-390f-a29d-a80f89dc3bd1 | -15.0729 | -48.6522 | 2026-08-14 00:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 11a8beda-40e8-3485-b301-5c05b152cb20 | -21.9049 | -55.3755 | 2026-08-14 00:40:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 635dc69f-a5b2-3142-8140-2ce4b4519a05 | -15.1362 | -41.561 | 2026-08-14 00:40:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 47.4 |
| ac377f67-9ffb-3d7b-9dd1-998c4b5cb01c | -6.6194 | -59.0609 | 2026-08-14 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c3b51253-9c5d-3b1f-b29d-209c6f4bf3a7 | -14.4734 | -45.6914 | 2026-08-14 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 747d6b4e-cc86-3b0a-9190-2dffcbb41bcc | -11.4887 | -54.6068 | 2026-08-14 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 402d4946-76f7-3ead-a83b-6ca2ab605aa9 | -11.4885 | -54.6273 | 2026-08-14 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| c8c8f105-85db-3d49-94c5-2d149f2864fb | -11.5074 | -54.6256 | 2026-08-14 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |


[Clique aqui para ver as próximas entradas](README5.md)
