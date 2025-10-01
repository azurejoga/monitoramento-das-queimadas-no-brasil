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
| 95872b3a-329a-38c6-8df2-becf8fc9e0c3 | -6.05826 | -42.44687 | 2025-10-01 03:28:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 92abee99-695b-306c-8a6d-67cdca0ad11f | -3.93203 | -41.60177 | 2025-10-01 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 28f9f9cc-4c5f-32b8-a538-05920cf8be4c | -7.09421 | -45.56324 | 2025-10-01 03:28:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94b6932b-f60a-3429-9f0b-f478d61eda04 | -5.85781 | -43.4104 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d2e156f6-c068-31ae-8386-937c77307684 | -5.48412 | -37.38097 | 2025-10-01 03:28:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6660354f-15d7-3cb0-9b9e-0c192ab1ea18 | -5.61828 | -43.24039 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6755ec84-fe56-3572-ba6f-c4abeeb77d9e | -5.76161 | -42.86562 | 2025-10-01 03:28:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 96df2485-9d00-389f-a4b7-021f7b98b8bf | -6.81191 | -44.47564 | 2025-10-01 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 902a7373-fcb2-33f4-b690-4a06c6237070 | -5.85158 | -43.40926 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e939756b-3812-36fb-9301-d4cbd0d09554 | -3.35227 | -43.20152 | 2025-10-01 03:28:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87160b14-421d-3048-944d-5a1440e4b2fe | -5.95115 | -45.87411 | 2025-10-01 03:28:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8df21341-4b02-3cf8-805b-1bb6c5a24168 | -6.65876 | -41.40017 | 2025-10-01 03:28:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 063edaf9-ee60-357f-8541-586abb06ba48 | -3.74849 | -41.0363 | 2025-10-01 03:28:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0da56722-5c12-3898-a03c-86b524554883 | -4.22342 | -40.8063 | 2025-10-01 03:28:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79d6eee3-8e5d-3096-9ba8-2ae112ce4188 | -4.80598 | -45.33702 | 2025-10-01 03:28:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49a20951-8235-36cf-9702-37a58d3c5af5 | -6.397 | -41.76065 | 2025-10-01 03:28:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f933a512-27b7-38b8-9da2-1953efd8f628 | -7.16025 | -41.71152 | 2025-10-01 03:28:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d5bc4f62-0f84-3c13-8a70-864013249b79 | -5.40769 | -41.33107 | 2025-10-01 03:28:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac020cdc-f472-3a51-a0d8-066ad65cdd7f | -6.83185 | -42.98843 | 2025-10-01 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0ffe29e2-2b3f-3efb-a296-6b6027b8251b | -6.2082 | -44.23199 | 2025-10-01 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4bfd4a68-3e80-3ae9-add4-fc95eb53537d | -8.67635 | -40.95399 | 2025-10-01 03:28:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1b4c03e8-57eb-3916-b459-bbc8b32253b7 | -7.95398 | -41.41214 | 2025-10-01 03:28:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dd9eaaca-60ba-389b-900e-0425edc0d89e | -5.63742 | -43.9161 | 2025-10-01 03:28:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 71401103-a451-3d8d-b83a-92db32ef76d2 | -5.47727 | -43.07593 | 2025-10-01 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e79470f-9a2a-30db-8f3b-d05724b21d79 | -5.40708 | -41.33454 | 2025-10-01 03:28:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5720ed31-3b2d-3e4a-9057-daaa8e7e50d5 | -6.09889 | -42.68036 | 2025-10-01 03:28:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 86cdde42-725c-3a88-9c2e-6f134eb04f01 | -5.85343 | -43.39923 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1288dcf8-6d9b-3805-915f-9591354e2fb3 | -5.85252 | -43.40416 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e7a272e3-1552-3528-93ab-31dc9988da4f | -5.61913 | -43.23565 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75146c49-3c34-324b-bc9b-8563ecdbd6a8 | -5.85334 | -43.41143 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7ef4bb2a-4459-30cb-a965-f13f30f439bd | -6.09042 | -42.43579 | 2025-10-01 03:28:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 447b36de-9f98-3d11-894a-2ea94f109aca | -7.02185 | -44.46116 | 2025-10-01 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79320628-3f54-3959-9b5d-df958943b1f1 | -3.87855 | -42.52784 | 2025-10-01 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 720db511-0d3e-3bda-a72b-d743c737397e | -5.98328 | -42.65844 | 2025-10-01 03:28:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fe830284-18fc-3f62-b5d2-ead8103c3b7a | -7.16772 | -41.70151 | 2025-10-01 03:28:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| be6a6aac-d2b3-3104-8060-396b276a0e59 | -5.47641 | -43.08067 | 2025-10-01 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0761f24-3982-35c6-829f-1c2eaaebd772 | -6.0981 | -42.68468 | 2025-10-01 03:28:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b185cb2a-fbff-387c-b4df-93ecf2ded3ee | -7.01956 | -44.47351 | 2025-10-01 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37de08d0-82cd-3196-984b-30c527c88434 | -6.99156 | -42.80231 | 2025-10-01 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe04ed5e-8c79-3c21-a0b8-34510662b3b0 | -5.63546 | -43.92546 | 2025-10-01 03:28:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| cf9e5c67-03c2-3975-91b0-3ec01f9272a2 | -3.85571 | -40.43573 | 2025-10-01 03:28:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 034f74b8-7cbe-3fe3-9747-fb4ef0e59d1e | -5.64279 | -43.92176 | 2025-10-01 03:28:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c56f47f9-5f03-3bdf-a7b2-1d602dfa6adf | -5.63641 | -43.92017 | 2025-10-01 03:28:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f758ee28-d847-34a3-8990-add72ae6917a | -4.9603 | -42.04108 | 2025-10-01 03:28:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 66f600a3-a97e-3ee6-bc83-fcfb27d07cd5 | -7.79209 | -42.51151 | 2025-10-01 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 578178d6-75a3-34d0-a84b-5d643853c155 | -5.40518 | -37.69932 | 2025-10-01 03:28:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e24e5307-4c3c-37fd-99c2-7d7e9f9932aa | -6.08815 | -42.48241 | 2025-10-01 03:28:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 69353c65-fbd0-300f-a7bb-ce6f2ccc9d65 | -6.65938 | -41.39653 | 2025-10-01 03:28:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6d6d54cc-369c-3e97-9829-775272f5500a | -6.10178 | -42.68094 | 2025-10-01 03:28:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 17d38106-381d-349d-a6c0-f297aa0d0a5e | -5.33282 | -43.749 | 2025-10-01 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ffd4d978-f4b8-3f29-a6e7-8fa6599ef9d5 | -6.08229 | -42.48135 | 2025-10-01 03:28:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3227833d-ac5f-3e6f-af12-65633688c1d2 | -7.41265 | -45.41692 | 2025-10-01 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8d38be4-fcc2-3866-b588-33b12752a25f | -5.83418 | -42.80733 | 2025-10-01 03:28:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| eb71ddc9-f230-3e30-92b1-8dadbd9363b4 | -5.41429 | -41.32574 | 2025-10-01 03:28:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b8f85136-6201-3c20-939d-94751353cdfc | -3.7534 | -41.041 | 2025-10-01 03:28:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c89db210-6cc2-3b31-b34d-5a9b31358546 | -6.7961 | -44.74772 | 2025-10-01 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05595ed8-5523-383f-ae11-e9ab8afdf70e | -3.86102 | -40.43671 | 2025-10-01 03:28:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 441838bf-d7c4-384d-b599-228c5ef2ceb9 | -6.07294 | -42.67089 | 2025-10-01 03:28:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ef6deb74-c8d1-3e92-b55e-880b324b466d | -6.06388 | -42.68741 | 2025-10-01 03:28:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f71e110c-ca90-31c6-ad00-4dd9b9d827c5 | -7.0943 | -45.55614 | 2025-10-01 03:28:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75b9f6c7-f7d1-3d18-bb2b-3300350b4cbc | -3.86655 | -40.33922 | 2025-10-01 03:28:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1a7b4769-fadf-3a5e-8cfd-0dfb1b7416a5 | -5.64283 | -43.92286 | 2025-10-01 03:28:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 07c7b924-5de0-304e-98ce-7c2dca4c85d2 | -8.67847 | -40.95269 | 2025-10-01 03:28:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2be402d1-8061-37e5-9434-b7f1c2dcdb80 | -6.23843 | -45.34071 | 2025-10-01 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9adf7793-2036-34f0-91be-266d72dd03d4 | -4.00508 | -43.28524 | 2025-10-01 03:28:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2e0d1a4-f05c-32f1-8e08-9db32f32b4e3 | -6.43192 | -40.62336 | 2025-10-01 03:28:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0215c07-ad3e-3c66-b1fe-6faa36030826 | -5.98407 | -42.65412 | 2025-10-01 03:28:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 01c49f25-6893-3cbd-b423-4a8568070287 | -6.64434 | -42.03638 | 2025-10-01 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eab69333-7741-363f-9a6f-e179a983967c | -7.78639 | -42.51038 | 2025-10-01 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c8a43ec5-3154-3048-b726-b74eff489edf | -7.20865 | -39.96849 | 2025-10-01 03:28:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 293eeb9e-3826-3e3c-9405-f6c59ada8b2f | -5.47089 | -43.07884 | 2025-10-01 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d849feb-4abb-39a4-8864-79e96e18c435 | -4.6266 | -43.54904 | 2025-10-01 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 948785d1-bbb0-3378-8241-437d3b3cb93e | -5.47026 | -43.07957 | 2025-10-01 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 035c1e7a-5ec4-3452-b133-7130c06ac709 | -7.62656 | -45.45222 | 2025-10-01 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5de074a4-5e3c-3eb0-93b7-673945c18853 | -6.23285 | -45.33233 | 2025-10-01 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63d5fee4-28b5-3734-98d0-febc7b1b17f7 | -6.16786 | -43.09647 | 2025-10-01 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e701db1c-cbaa-3668-8185-ff4254b8a183 | -7.62536 | -45.4586 | 2025-10-01 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3ea71d82-8e54-38d6-a521-3eb2d1bd6a96 | -6.64151 | -42.03452 | 2025-10-01 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ee1dfee-db8a-37d7-8a8e-60174be20057 | -6.79043 | -44.74115 | 2025-10-01 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20dd1d97-2834-3aaf-94e1-1458dbb5fc08 | -3.41287 | -40.2176 | 2025-10-01 03:28:00 | NOAA-20 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1c8c14d-fbb9-37d8-a48a-e212a345784c | -6.79224 | -44.75048 | 2025-10-01 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13462eac-6e43-3805-a5ed-e54385e27893 | -6.79712 | -44.74215 | 2025-10-01 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc88c092-7435-3a1f-a342-51cc4aa4d6f3 | -5.75996 | -42.86659 | 2025-10-01 03:28:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8731ecf6-f13c-3a40-9b9c-8064e65d5610 | -3.88546 | -42.52421 | 2025-10-01 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6f9561c7-2065-37d7-b84a-b8e3f421c632 | -3.93023 | -41.5772 | 2025-10-01 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5639e6f4-3497-3619-a100-9045a6c0e46e | -8.68197 | -40.95196 | 2025-10-01 03:28:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 91ff762c-dcf0-3e87-b31c-6e1fe288a490 | -7.17386 | -41.69881 | 2025-10-01 03:28:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8236d354-e8c0-3c46-b141-ecf4fbe5b479 | -6.10101 | -42.68534 | 2025-10-01 03:28:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d7e93374-adcb-381c-ad95-ee18fd7cfcbf | -6.37386 | -45.61032 | 2025-10-01 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| af8847b7-cfff-3de0-be6c-26c337627733 | -5.63547 | -43.92656 | 2025-10-01 03:28:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e0091ab6-a85b-3e76-968a-8d3dc067f274 | -5.33188 | -43.75425 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d144445a-11a4-3cd0-a683-a4eb913cba50 | -3.74721 | -41.04385 | 2025-10-01 03:28:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7af74342-b488-3814-91e9-9b96f958f6d8 | -6.35084 | -43.41043 | 2025-10-01 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 38c0c2a0-6f2b-3811-b03a-90b1e84a01bb | -6.87104 | -39.27446 | 2025-10-01 03:28:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 27941f05-b398-3b9d-b40c-424796f339ec | -5.40019 | -37.70267 | 2025-10-01 03:28:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79da38c8-bede-3d8c-8f99-2aada03d98ef | -3.35086 | -43.20124 | 2025-10-01 03:28:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8767fef9-fd1f-3857-8bbb-41bd0bace63e | -4.00601 | -43.27993 | 2025-10-01 03:28:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 815444de-1576-3737-a507-1e79e5353266 | -3.87937 | -42.52316 | 2025-10-01 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 528b2ae8-0084-3529-b8d1-c4bfe2b6ccf8 | -5.76766 | -42.8666 | 2025-10-01 03:28:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 12e883bc-ba13-3841-8944-94da7e7f04bf | -3.93336 | -41.59379 | 2025-10-01 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README14.md)
