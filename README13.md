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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6494845-6f5c-3346-a9cd-d0714b5b1eb9 | -7.3666 | -38.9837 | 2026-09-17 02:00:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 1fac1c36-fcba-37e6-8640-183e73885b15 | -12.5094 | -50.8664 | 2026-09-17 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ae91f3c6-78e5-3dd7-8ca0-986b84c81ec7 | -13.3758 | -57.026 | 2026-09-17 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 3cfe3476-cb02-30d8-a29a-8aa358afdfb6 | -6.8962 | -59.0303 | 2026-09-17 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 393a230b-b107-3ca8-a0f5-2aab7ab3622d | -8.4983 | -57.6271 | 2026-09-17 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 4c89e5d1-b30e-3e15-a0cf-0411e2aa390c | -5.7756 | -45.0826 | 2026-09-17 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| da1d3755-3a52-34cf-ad2a-e90ce40b6bf8 | -3.4757 | -54.6972 | 2026-09-17 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 2387c6fd-56c8-3634-a89a-9475f65cc2c9 | -5.7567 | -45.1067 | 2026-09-17 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f92e81b5-9241-3f38-add7-3c72cdd1c602 | -2.9581 | -50.3359 | 2026-09-17 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| bb5746f3-a680-3dea-9df2-d05ad0801d24 | -8.4982 | -57.6468 | 2026-09-17 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| cc258ca2-b695-3739-83e1-53a7826c3528 | 2.7086 | -60.2969 | 2026-09-17 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 87a2bc68-c91c-3954-9dd7-4be3970e053a | -6.9309 | -63.0301 | 2026-09-17 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 4663f78e-7d70-35cb-bc87-2ab763ba02b2 | -9.112 | -45.7294 | 2026-09-17 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 1589d17c-3d35-3504-b87d-785c950e2ff5 | -7.3666 | -38.9837 | 2026-09-17 02:10:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 933e06c2-b507-39ef-8c03-54571f5cafd6 | -5.7756 | -45.0826 | 2026-09-17 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| da48ec87-f07d-3ae8-9287-77b63980b0d4 | -5.7752 | -45.128 | 2026-09-17 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c021feda-c905-36e3-a9af-63b16edb43a8 | -5.647 | -44.8192 | 2026-09-17 02:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| cdffa091-75c2-3eab-aa54-c50a7e4f7b5f | -9.8884 | -48.3794 | 2026-09-17 02:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 9551e6f5-1abc-379b-add6-2b2d0fb71f2d | -6.3656 | -58.2966 | 2026-09-17 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 54ed6cb3-347e-301b-8275-af73e6a4d593 | -10.8343 | -54.0933 | 2026-09-17 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 5a10a927-21fc-3355-957e-e77e083e2c05 | -9.1123 | -45.7067 | 2026-09-17 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 01ba9732-187d-3548-95fe-94878d4e5cfc | -8.4796 | -57.6478 | 2026-09-17 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ae4dbf4a-2f92-35c4-b314-8b596c5bbbda | -5.6285 | -44.7977 | 2026-09-17 02:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| fdd4e940-0f2f-3cf2-b51d-f11d190d14f2 | -2.6965 | -57.6278 | 2026-09-17 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d7c6fc21-5c8f-3753-9058-f44824a9726a | -8.4982 | -57.6468 | 2026-09-17 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 258944dd-dd2b-3160-a6ab-1d261ca2ada2 | -10.834 | -54.1138 | 2026-09-17 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| af83831a-2289-31cf-8e22-a84a952cbee5 | -4.5587 | -42.9523 | 2026-09-17 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| a5fa792b-4118-38a5-9e8a-80b89fb1980a | -5.7941 | -45.104 | 2026-09-17 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 25a92a2d-021b-39c3-8bc2-4ebd7461606e | -5.7754 | -45.1053 | 2026-09-17 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 320.1 |
| ac73eba3-7156-3c47-9961-ea822ef65bfd | -3.494 | -54.7166 | 2026-09-17 02:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 69341a18-c92e-35a2-bfb0-fb3e7dad592b | -5.6283 | -44.8205 | 2026-09-17 02:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 9c8311d8-2a2b-37dd-942d-f6034fe9b1a0 | -9.8694 | -48.3814 | 2026-09-17 02:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 79a333f4-638e-33a9-a035-4a87ad2c6dcf | -9.112 | -45.7294 | 2026-09-17 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| a650bfaf-d173-3b45-8637-5132b5a86484 | -6.9309 | -63.0301 | 2026-09-17 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| cf9442f1-0ac9-3197-852f-7db322a36ff8 | -2.6966 | -57.6084 | 2026-09-17 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 79595ad2-8501-309b-8f80-dd28a29f2fb9 | -8.4983 | -57.6271 | 2026-09-17 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 3a4e7a3d-a57e-3077-8f6f-1f1fdb6c9077 | -2.9581 | -50.3359 | 2026-09-17 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| fc25bb20-5db0-35ea-88bf-fec8e88092b7 | -5.6472 | -44.7964 | 2026-09-17 02:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 53a364bd-2f96-3476-b420-9b2ebf036b5b | -2.9582 | -50.3149 | 2026-09-17 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8a6298b0-b9f1-3851-a66f-6c6d31421803 | -3.4757 | -54.7171 | 2026-09-17 02:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 74e70962-9160-3f03-a80b-1cfd8986bcbb | -3.4757 | -54.6972 | 2026-09-17 02:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 7069142a-4bd3-3333-9007-c08c9566ece0 | -14.1405 | -48.7317 | 2026-09-17 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6d9682dc-f481-38f8-ba50-e263cba9edfb | -5.7567 | -45.1067 | 2026-09-17 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 166.8 |
| b8bce6fc-40a6-32b7-a808-c7e951f2dfdb | -5.76 | -45.09 | 2026-09-17 02:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad4bfae8-2274-36b1-b92c-0df86c54d293 | -5.64 | -44.8 | 2026-09-17 02:15:00 | MSG-03 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2d6c1d0-a677-34da-8ee5-b46e83ed2fd3 | -2.9582 | -50.3149 | 2026-09-17 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 17b7078d-ad12-38e3-a223-e2889d16f922 | -9.1123 | -45.7067 | 2026-09-17 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2af3c44b-c74b-3de7-b714-738a6962ea9a | -2.9581 | -50.3359 | 2026-09-17 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 52581d4e-6c08-3074-9b7d-09825a2fa468 | -12.491 | -50.8259 | 2026-09-17 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 1e0dd7af-36d7-3b13-8d6e-2e383823796e | -9.131 | -45.7273 | 2026-09-17 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 2d24d9f1-f512-3ae7-82fc-3eccc4383484 | -2.6966 | -57.6084 | 2026-09-17 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 8bc60f3b-695e-3378-a884-f3fbaa1af635 | -5.7754 | -45.1053 | 2026-09-17 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 314.5 |
| bb3284ec-3728-3ff2-b0c9-2e4229175fc0 | -6.3656 | -58.2966 | 2026-09-17 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a23da6c2-bf6b-3403-89c7-8a495a5528ea | -14.1211 | -48.7347 | 2026-09-17 02:20:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 65614d46-6f1c-383b-abe8-f69b451b631f | -9.112 | -45.7294 | 2026-09-17 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.9 |
| c5c41cae-9eb1-3629-a175-bd9a11e85d92 | -12.5097 | -50.845 | 2026-09-17 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 10747e34-4494-38a4-94e5-5b4f076345dc | -5.647 | -44.8192 | 2026-09-17 02:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 8b9a3659-d8bf-3198-b46e-5f9e77a3e2a0 | -5.7567 | -45.1067 | 2026-09-17 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 2e481d94-cde2-3cad-8145-170da0a80999 | -6.7093 | -59.4623 | 2026-09-17 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 24867770-cdfa-3171-9c3d-a60aefc04e14 | -12.5118 | -50.7164 | 2026-09-17 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 97d1ae23-1a77-38ff-8c38-b1bca2393c52 | -3.4757 | -54.6972 | 2026-09-17 02:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 22f2f92d-7d0a-3379-848e-4c3a42055cc9 | -12.5121 | -50.6949 | 2026-09-17 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 3c1fa14d-2dff-3989-a0cb-60b2f9959836 | -5.7941 | -45.104 | 2026-09-17 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7ef653d3-814e-33c7-92ab-a8c70cbac5aa | -5.6472 | -44.7964 | 2026-09-17 02:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 29b273a3-71ce-3784-9bbc-822b50dc2943 | -5.6283 | -44.8205 | 2026-09-17 02:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 5897fb44-43f2-333f-9dad-85ad4ac2af61 | -4.5587 | -42.9523 | 2026-09-17 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a91b1d7a-85d1-3df3-b3a9-77728bb189d8 | -2.6965 | -57.6278 | 2026-09-17 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| f116be57-b75e-39b5-abef-0741883439ba | -8.4983 | -57.6271 | 2026-09-17 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 50741012-cb6a-3f70-ae7e-e29a83cf9e5a | -9.6091 | -45.3544 | 2026-09-17 02:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| de277c1e-2084-3cce-bcf5-026451247035 | -5.6285 | -44.7977 | 2026-09-17 02:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 351e86e0-c589-3d2e-9932-ac6766cd3ff7 | -14.1405 | -48.7317 | 2026-09-17 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 63b8fd8e-0f27-3400-a40e-49424ef6050d | -12.4903 | -50.8687 | 2026-09-17 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| abc4ce37-f869-30a3-8ffd-bb23af8f3418 | -8.4982 | -57.6468 | 2026-09-17 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| eabc26eb-0cc0-359c-8d91-3ac6a8376123 | -3.494 | -54.7166 | 2026-09-17 02:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b2a26cca-a29d-3577-b51a-8fc823355987 | -5.7752 | -45.128 | 2026-09-17 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d7d9b714-912c-3cc7-a8e4-a1359baa6a87 | -10.8343 | -54.0933 | 2026-09-17 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 2888ffcb-c4e7-3b71-a245-1e6b2acffcae | -5.7756 | -45.0826 | 2026-09-17 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| a15377df-47df-35c3-a653-ff2d98111127 | -9.8694 | -48.3814 | 2026-09-17 02:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d8633eb1-a174-38f2-a22e-a569151f900d | -12.4906 | -50.8473 | 2026-09-17 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 95c20019-d62a-3461-8768-0693ed7e06da | -8.4796 | -57.6478 | 2026-09-17 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7d9f2ba0-eef2-3a77-b059-85bb43c5d4ed | -6.8031 | -59.1886 | 2026-09-17 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 5028bcfd-dcbd-336e-a57d-34ef15450ea2 | -10.8532 | -54.0916 | 2026-09-17 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9200f865-3350-3c49-8473-1fc2fe58b748 | -3.4757 | -54.7171 | 2026-09-17 02:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 2d7ea08e-f76f-376a-b6b1-b0fa610ed0c5 | -8.4796 | -57.6478 | 2026-09-17 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 606e85eb-62e0-37bd-b034-2ed44f83b919 | -9.6091 | -45.3544 | 2026-09-17 02:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 6df81859-c980-3549-bd53-9fd4af05fe33 | -2.6965 | -57.6278 | 2026-09-17 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d01d3199-18f8-3552-8abc-6faee079463b | -2.6966 | -57.6084 | 2026-09-17 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 277faa2a-d25d-3e54-9e57-95f2c9158e71 | -5.7754 | -45.1053 | 2026-09-17 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 361.0 |
| 4192c7d4-e813-3a51-a22a-1d61bccb16f5 | -9.131 | -45.7273 | 2026-09-17 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 7e2958ec-cd4b-3a77-b951-4661717d8950 | -5.6472 | -44.7964 | 2026-09-17 02:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 205.2 |
| d7928c0b-7d1e-3a3b-b48e-9fd304cde9cf | -5.647 | -44.8192 | 2026-09-17 02:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 70d334d9-bed7-3a55-a947-5c5f820c087e | -6.8962 | -59.0303 | 2026-09-17 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9852a32a-8ae8-3fea-a082-4efb1170851a | -10.8343 | -54.0933 | 2026-09-17 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 89c24b92-a975-393e-a78d-5ad5c4416408 | -3.4757 | -54.6972 | 2026-09-17 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2d5907c9-000e-3136-b0e2-6baae63cc9fc | -9.1123 | -45.7067 | 2026-09-17 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 8f5f39eb-761c-30ea-a044-a9acfc7f2b8e | -6.7093 | -59.4623 | 2026-09-17 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 54f9a461-0733-3e7b-b47e-29fd245de7e9 | -8.4982 | -57.6468 | 2026-09-17 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 91af0710-04a7-3afd-89d3-60198d652249 | -5.7752 | -45.128 | 2026-09-17 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 7c4c724b-b2d8-32bd-ac80-462fc624104b | -5.7756 | -45.0826 | 2026-09-17 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| f7e4c9dc-91c2-39ec-bd89-69760ab7e1af | -5.7567 | -45.1067 | 2026-09-17 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |


[Clique aqui para ver as próximas entradas](README14.md)
