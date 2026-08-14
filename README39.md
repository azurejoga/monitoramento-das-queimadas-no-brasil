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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af282776-9f6b-3809-b219-10360a317036 | -11.4677 | -44.5791 | 2026-08-14 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 8204a838-eaf2-3e00-b2aa-fe089adc00ba | -13.2798 | -54.2435 | 2026-08-14 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 0ad9493f-f517-3871-8bf5-a388cf84adee | -9.9896 | -53.9404 | 2026-08-14 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 0d1d9bb6-899b-3e1a-822f-ffb57167732c | -13.2801 | -54.2228 | 2026-08-14 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 76e6e4c9-a635-3df0-87cf-cb3d23545fc4 | -9.49 | -51.6248 | 2026-08-14 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 09261541-48d2-3168-a0c9-e5407ca6f6ae | -11.9369 | -47.3143 | 2026-08-14 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 267.6 |
| 5a949de6-b801-3503-8aef-5c8e169c5d4d | -12.1583 | -50.1365 | 2026-08-14 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| b039a5e7-1997-31c4-afd8-08f71ee85094 | -11.9365 | -47.3367 | 2026-08-14 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 2c7f417d-4b67-32ed-94f8-b6119237dc78 | -6.9685 | -59.2976 | 2026-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 173.8 |
| eda8d16c-88da-3396-841e-3ec28656ffb0 | -6.2571 | -47.6738 | 2026-08-14 14:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 81efdfc3-43ef-387d-be29-7297cc678528 | -14.075 | -53.6135 | 2026-08-14 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 0c8e4afd-1194-3df1-85ed-013c4c545c65 | -10.6909 | -50.5165 | 2026-08-14 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 433b7dcb-c074-39fe-9842-18fde097cc6c | -13.2804 | -54.2021 | 2026-08-14 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 82ebabaa-ca3f-3452-998a-812d46be0220 | -9.9894 | -53.9608 | 2026-08-14 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 208.1 |
| 118807c6-7e29-33c2-8469-6e5abc699417 | -10.7099 | -50.5145 | 2026-08-14 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 0108f4ab-819f-3615-9b9f-4b80234db1c0 | -11.0635 | -50.9452 | 2026-08-14 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 033e31e1-8eea-35cc-aa72-08359ee07d4e | -13.2801 | -54.2228 | 2026-08-14 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 63865107-2450-3a52-b644-329e468db2d1 | -9.9896 | -53.9404 | 2026-08-14 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 70d9ad12-b35e-3ad5-9878-cdd322a5361c | -6.9847 | -45.8685 | 2026-08-14 14:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 66d22d10-372d-3963-b0f1-4dc12e682454 | -9.9894 | -53.9608 | 2026-08-14 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 209.8 |
| e85de723-30fc-33c3-91a1-389b892b0e50 | -6.9502 | -59.2791 | 2026-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 82734e06-19f0-37d4-85ee-a8aaa977ca58 | -13.2798 | -54.2435 | 2026-08-14 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.5 |
| c601474f-5a51-3db4-9fab-5d7a8a8d2e01 | -11.0443 | -50.9685 | 2026-08-14 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 13934ca1-1af1-3959-b591-8c5b6a6d751d | -14.2752 | -51.966 | 2026-08-14 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 04eae300-d850-32a4-9712-ff2e91ad3a0f | -13.8227 | -53.7889 | 2026-08-14 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 566fbc15-0c94-3c04-9cce-0646f805893d | -11.9737 | -47.3986 | 2026-08-14 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 1115a85c-c3cd-39e2-88dc-090b77847298 | -11.4885 | -54.6273 | 2026-08-14 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a98ad360-7179-3b69-8a71-6eda38d22722 | -7.5851 | -61.228 | 2026-08-14 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d9aa58a6-e68c-34d9-ba90-d867b987e2f0 | -11.6015 | -54.6577 | 2026-08-14 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 587ac489-6cd5-340a-9e67-27c8cedfbbc4 | -11.7128 | -47.0088 | 2026-08-14 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 9e2da4b9-6618-3d71-8bab-56b80b3dd789 | -6.95 | -59.2984 | 2026-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.3 |
| ccfdb5ed-72de-3e15-ae78-c406f5f26deb | -14.0561 | -53.5949 | 2026-08-14 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9e9402f4-f688-3dee-8bcd-9a52d9484f3f | -6.9686 | -59.2783 | 2026-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 8459cb4a-9f62-3b71-92e7-374a73fbf49a | -11.956 | -47.3117 | 2026-08-14 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| bc4e0031-d947-3ce9-86a3-6a8adf868820 | -9.9708 | -53.9419 | 2026-08-14 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| b4791d24-4f39-3bf9-8a0f-1d157a2b050d | -10.7099 | -50.5145 | 2026-08-14 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1d270060-b875-344b-afc3-1cb96615dfdc | -6.9685 | -59.2976 | 2026-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 8c88fc4a-4fb6-34df-93d0-4f6dcfd79dc4 | -11.4677 | -44.5791 | 2026-08-14 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 21435b57-411f-3e83-a278-576b1190e567 | -11.0635 | -50.9452 | 2026-08-14 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 187.7 |
| caf92367-92dd-3159-b0e5-f9af31412904 | -7.0146 | -41.445 | 2026-08-14 14:10:00 | GOES-19 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 51237e2f-a982-3915-85b4-fad68534a12a | -13.2804 | -54.2021 | 2026-08-14 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 3f67657a-84ce-3f4c-aa05-46849bf0a985 | -14.2945 | -51.9635 | 2026-08-14 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 6578cfbe-eb99-39dd-aeb1-2d816c15afd2 | -9.9706 | -53.9624 | 2026-08-14 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 151.4 |
| c1ee75ee-54e5-32cf-99f5-b1b4facb838b | -13.6859 | -46.2624 | 2026-08-14 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 371c6baa-d55d-339d-a992-7f2e66b54fc3 | -6.95 | -59.2984 | 2026-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 195.5 |
| 1840eab7-4e8a-350b-98ff-0c8aa716c41f | -11.4885 | -54.6273 | 2026-08-14 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ef75e05f-646d-3544-91de-3819f149368f | -11.6015 | -54.6577 | 2026-08-14 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| ed097068-e280-33c9-adf5-173ade31a1f6 | -11.5074 | -54.6256 | 2026-08-14 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 2c0788f5-52da-378f-b51e-e69f8852195d | -11.0635 | -50.9452 | 2026-08-14 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| a2c9c198-45b5-3e10-b03a-bcb1575e82eb | -14.2752 | -51.966 | 2026-08-14 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 983a87bb-a935-3edd-ba60-955e41dd487d | -9.9708 | -53.9419 | 2026-08-14 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 31e6c747-6d61-32c2-9868-de0a920d4bfe | -6.7871 | -58.764 | 2026-08-14 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 54029259-5100-34b0-9474-7812191ca6f5 | -13.2801 | -54.2228 | 2026-08-14 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 7057142f-8c1c-3f32-8b9c-898414cf76e7 | -11.4677 | -44.5791 | 2026-08-14 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 39878708-6072-3bda-b9e0-d0dc088bd81b | -11.6013 | -54.6782 | 2026-08-14 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| c7dc43b6-950f-3931-b96b-519feb257e81 | -6.9686 | -59.2783 | 2026-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 218.1 |
| c99c1f63-e76c-3198-a6f5-013d93799bd7 | -13.8227 | -53.7889 | 2026-08-14 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| bc966149-eae6-39ff-99df-0c3a08381471 | -7.5851 | -61.228 | 2026-08-14 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ad1054b1-ec7e-32af-958f-3074ca6e19c0 | -9.9706 | -53.9624 | 2026-08-14 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 197.6 |
| b6488420-0077-3598-be9e-23598be4b6b7 | -11.956 | -47.3117 | 2026-08-14 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| be50a383-d81a-36f1-a00b-d9c081887f3e | -13.2804 | -54.2021 | 2026-08-14 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 953a8e0f-4c29-3cb9-94ee-69a294073ae8 | -6.9502 | -59.2791 | 2026-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 2de5958e-8197-37ee-92d5-784a1cf0e0de | -14.2945 | -51.9635 | 2026-08-14 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| d5953401-256e-3303-ad85-0b83c455eb79 | -9.9894 | -53.9608 | 2026-08-14 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 197.5 |
| 64e657cb-322e-3096-81b8-9a9682e7d8e7 | -6.6379 | -53.4177 | 2026-08-14 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 54e738ae-ac79-3683-9415-9dd1196e88f1 | -7.0146 | -41.445 | 2026-08-14 14:20:00 | GOES-19 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| a2953c6a-ade3-3b2b-80a3-94560ec01e7c | -11.9369 | -47.3143 | 2026-08-14 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 50cf4a5c-fd5b-3717-8df3-f55357add4b0 | -9.9896 | -53.9404 | 2026-08-14 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 4c238a1b-9790-3025-92ea-758cfb433e84 | -12.0099 | -46.4044 | 2026-08-14 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6588b8e6-bf49-3cae-b944-cf879fb6b851 | -6.9685 | -59.2976 | 2026-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 191.0 |
| ec783f53-2f29-30b6-a12c-3728a7c2d585 | -14.8232 | -52.6582 | 2026-08-14 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 9e7e7769-cd16-3df3-a343-c612d61b5857 | -9.7584 | -60.7645 | 2026-08-14 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 666cb982-53e0-3035-8b80-97a994dd7fb6 | -12.1583 | -50.1365 | 2026-08-14 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 8ae10466-a250-3be4-a7f8-169bec7a92d1 | -6.95 | -59.2984 | 2026-08-14 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 8a3ac040-7834-3517-8977-ea9a0f151e29 | -11.6015 | -54.6577 | 2026-08-14 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 148.5 |
| de078709-78bc-3e2e-825a-e4d9888906e7 | -13.2801 | -54.2228 | 2026-08-14 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 134bf940-266e-3ff1-805a-0ce8defec5b0 | -9.9894 | -53.9608 | 2026-08-14 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 264.8 |
| f0373046-3ba7-3b6f-b660-4b7c8efd11df | -15.1115 | -48.6682 | 2026-08-14 14:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c1505ba1-eb05-3154-a105-f5bd5439affc | -13.8227 | -53.7889 | 2026-08-14 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| bb33d45b-8292-3312-b265-6e86c02e015c | -14.2386 | -53.0071 | 2026-08-14 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 901a5d14-530f-3f81-99f9-75064c5d6826 | -6.9686 | -59.2783 | 2026-08-14 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 2a8aebb4-ca77-300c-b140-44bacd56ec9d | -14.0365 | -53.6181 | 2026-08-14 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 730f6520-527e-33e9-863b-6a1768aa5f66 | -6.9685 | -59.2976 | 2026-08-14 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 179.0 |
| 37cf7cd6-dade-3374-9ffc-ef97b2155812 | -10.7099 | -50.5145 | 2026-08-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 1825ba13-41b1-339f-a19a-cf8d82387ede | -11.0635 | -50.9452 | 2026-08-14 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 73b037f1-d07e-3a10-9731-4c38405a11f5 | -11.6013 | -54.6782 | 2026-08-14 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 4990c8f5-eaa8-369e-a7fe-72b443667d07 | -14.0936 | -53.653 | 2026-08-14 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| f8959138-a4c3-34a9-9566-17260dc83930 | -6.9502 | -59.2791 | 2026-08-14 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.6 |
| a3815c2c-e253-3c0f-a793-647ae7eaa71b | -11.9737 | -47.3986 | 2026-08-14 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| bd3e513b-6b9f-30b7-90e3-3df0ca72416e | -14.3526 | -53.098 | 2026-08-14 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| fd565665-3fb9-3cf3-9bde-165031f88fa5 | -14.2945 | -51.9635 | 2026-08-14 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| cc78075f-dfe7-373d-afca-5b06c1dd913f | -14.0561 | -53.5949 | 2026-08-14 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 50ded0d3-5fd5-3316-b252-d74adf9018cc | -7.0146 | -41.445 | 2026-08-14 14:30:00 | GOES-19 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 34cd7655-9451-387c-8e40-e0f79373dd61 | -9.9708 | -53.9419 | 2026-08-14 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 329ae6c9-7e6c-3d92-8a62-369ab11ae69e | -11.4677 | -44.5791 | 2026-08-14 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| cc2ec6bd-ac47-3c6e-b87f-72f6515ffbdd | -14.3719 | -53.0956 | 2026-08-14 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 2da3d136-819d-3fef-8110-857b42a47a61 | -15.0553 | -52.6698 | 2026-08-14 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| c0a958a5-a6be-3649-b36f-cca0dab447fd | -14.2752 | -51.966 | 2026-08-14 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 94a930e9-cdb4-3380-8fd7-0b584e34dcfa | -6.7871 | -58.764 | 2026-08-14 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| ee1b7f14-cba5-357c-a1e5-e3aed40ede39 | -14.2389 | -52.986 | 2026-08-14 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |


[Clique aqui para ver as próximas entradas](README40.md)
