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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 040ba372-2d2b-3ff7-8fd6-8b355306808b | -5.16881 | -38.14205 | 2026-08-28 16:05:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 561ae45b-2dcd-31c0-8045-8b1449c446c8 | -12.78368 | -40.8219 | 2026-08-28 16:05:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9a328551-cc6a-3936-ad5c-0d604c0f08f7 | -12.49568 | -43.77365 | 2026-08-28 16:05:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 44270b7f-4224-348c-a2f1-4287c18eaef2 | -8.16862 | -46.17074 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2023694-4a38-39ef-8242-784a2a1afc96 | -8.82674 | -49.63495 | 2026-08-28 16:05:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4f89eb41-bf98-3bd4-b9a4-d5b2c5eda4ad | -8.78196 | -50.06494 | 2026-08-28 16:05:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0677bdf5-fa95-30dd-b28d-cb3fb93aa6f6 | -12.57256 | -48.48282 | 2026-08-28 16:05:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 61d8f8cc-9a96-3b28-98d9-ee7cbca79cc7 | -13.32202 | -48.19654 | 2026-08-28 16:05:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ff8b7f1a-8a6f-3b67-b478-ccd4c79b9ddc | -8.47791 | -44.7986 | 2026-08-28 16:05:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f78674d9-4fa7-3a35-9795-40b2152ee8ef | -5.33596 | -37.03901 | 2026-08-28 16:05:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 12f93f3a-d108-3ba7-add0-f9c700bbf6a7 | -7.0999 | -42.16505 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1cf3e1d5-15cd-3785-b57a-a679d61cb4e5 | -8.07647 | -45.83292 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2f2369ee-b9fb-34fe-89e9-9487b9b7af87 | -9.49213 | -45.62492 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cb5e0fb4-1e6f-3f45-8866-baeb71da968b | -8.77921 | -50.05953 | 2026-08-28 16:05:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| e041774e-a691-31a7-a379-8dd80c65b26a | -14.07922 | -42.29971 | 2026-08-28 16:05:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 7cc6fde8-cc03-37d8-a52a-288b26d8b878 | -19.65537 | -48.00576 | 2026-08-28 16:05:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce7f2ce2-afc1-3d96-b355-04df13d08b88 | -5.96002 | -44.80772 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| c5dcc7f2-67ed-3e7f-a468-3ca62bd61dff | -13.60724 | -45.77833 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cd06d500-5e14-353c-848d-272970f648b6 | -7.52492 | -44.45561 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 524d648a-f482-3417-abf4-f3eb7ff2b1b8 | -8.2868 | -40.86559 | 2026-08-28 16:05:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 8dcca989-7d7c-392b-8364-77400876dafb | -9.49608 | -45.65433 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| e98df196-88a6-3de0-838d-403cee9f6d32 | -14.22754 | -45.25012 | 2026-08-28 16:05:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f8dc9bca-3861-398b-989a-b677953d66c8 | -14.30183 | -41.50695 | 2026-08-28 16:05:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b8dc0fd7-43f9-3f65-b10c-6dbfe33e500d | -12.38478 | -48.19949 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d9a33175-f70f-34f5-8410-9333510e9078 | -9.63866 | -48.27628 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 941be27f-d927-305a-a66a-46db830e06f1 | -7.06095 | -43.58583 | 2026-08-28 16:05:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0facd31e-04b9-3f67-a757-208a0b768443 | -6.96514 | -42.0794 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 6c166c3b-9840-384d-83ed-c77272a8f192 | -13.00789 | -45.0429 | 2026-08-28 16:05:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7eb2fb37-a2ab-347c-893b-ad558d1f8e78 | -12.27271 | -43.14145 | 2026-08-28 16:05:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 3f8799d2-a9dd-3565-a391-723cb46755e1 | -6.86766 | -37.39962 | 2026-08-28 16:05:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 05bd46d7-6fec-3c07-9741-7b93443dff17 | -12.29069 | -43.14547 | 2026-08-28 16:05:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f8f6cfaa-c6c4-356c-8365-fc793cf22069 | -6.84729 | -42.8579 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6b766374-1bd7-3b05-81e3-d0298f1082ee | -6.9013 | -43.64419 | 2026-08-28 16:05:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 6b1ee970-c259-3de7-80d6-22d463e3d0c8 | -8.06687 | -45.83723 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 7257e0d0-fe64-31e8-95e3-edfd8ef96832 | -5.95437 | -44.78332 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0ff8739f-2057-37bc-8024-cd6589ee37d4 | -13.31825 | -40.90203 | 2026-08-28 16:05:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 571dec38-7603-3e28-9689-b32b068bbd9f | -13.82594 | -42.17203 | 2026-08-28 16:05:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 05311eb5-85b2-3173-afd8-dceb7f28e691 | -7.07616 | -42.20592 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 4d8686ed-f130-3d4b-9e29-07ca49750698 | -11.46379 | -40.86999 | 2026-08-28 16:05:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8fecf71a-b18e-38df-b165-27909e5731f1 | -7.07931 | -42.20052 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ac78123f-440e-33d5-9cde-8b086956261e | -12.66011 | -38.78372 | 2026-08-28 16:05:00 | NOAA-20 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 5cfaea6a-1dea-39cd-b3fe-126301fda56d | -9.48906 | -45.64017 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8afee626-8f54-361a-a29c-6aaeb0ad2360 | -14.93876 | -42.19543 | 2026-08-28 16:05:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7f582be1-bdf4-3a23-8ac2-97404092d31e | -7.08199 | -42.80571 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 2f5d7847-24f9-3059-b002-0df0ddcc60ee | -17.80617 | -42.24727 | 2026-08-28 16:05:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 419f046d-f0fd-3dcf-b38e-53ab8f4a50ff | -8.82751 | -49.6384 | 2026-08-28 16:05:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 06078138-1f84-3bdf-90f3-66f1e5474ac7 | -9.15816 | -49.96622 | 2026-08-28 16:05:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| d8b49543-b828-30cf-8c83-b24c3269f437 | -7.6069 | -45.8299 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 762bfbec-0cfb-38e9-b128-a114e3157ffa | -9.15224 | -49.97277 | 2026-08-28 16:05:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| ce137a1a-015d-32a5-aa63-2eb7b60e6175 | -7.62965 | -44.81249 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ed4eac4-33e8-3f3a-9b24-ee8a79aece4a | -14.82413 | -45.5189 | 2026-08-28 16:05:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 67e7b601-83d7-3757-a5b9-4cc7e248203d | -9.70871 | -48.13484 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3c7fed03-ea45-33f2-be32-204fecc81e3d | -15.16506 | -41.26806 | 2026-08-28 16:05:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1748e976-3a97-3c14-b236-da4109f710f0 | -9.48827 | -45.6343 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fa0113c2-231e-300a-a89e-42271b0b1bd1 | -7.11762 | -43.17326 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e1219283-4195-3771-ac25-1aa1029601a7 | -8.08722 | -45.83719 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68af4a62-2632-3f23-8861-544c6ddc8c55 | -6.84399 | -45.07469 | 2026-08-28 16:05:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5b82047e-3692-38e7-914a-5ce71b1259fc | -9.49293 | -45.63083 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 099d7e05-53ba-3219-9b56-5aa68ecf5d2b | -7.27989 | -49.94865 | 2026-08-28 16:05:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6da6645c-f831-3b69-9485-d8a6fc16e4bd | -5.9537 | -44.77871 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9597e729-429b-3a12-a028-fc7b8599c9d5 | -8.17552 | -46.16311 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07f0fde4-2ab5-3577-9091-bcd1999144b6 | -15.75382 | -44.32534 | 2026-08-28 16:05:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02abdc3b-0326-38f4-acbc-5158660a9e37 | -13.32839 | -46.90446 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3b3b47e3-c01e-3bdb-b224-2f1c7d7ad2ae | -6.87585 | -42.87498 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c46ae1f0-4ac6-399e-98b5-3392d8aae7a9 | -7.06994 | -43.58853 | 2026-08-28 16:05:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6f0deef0-4dab-3645-bb0e-f9db6194b869 | -13.11175 | -40.88317 | 2026-08-28 16:05:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| b7e201de-695f-3a16-b25e-0c758ae8e9d8 | -8.07685 | -45.83577 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a6567573-78d6-3f48-b626-a97230b81682 | -13.61262 | -45.77763 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1ada375b-d25b-3515-b29e-449be0ea18fc | -9.51003 | -48.02301 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c73f43c5-b978-3fe5-9b52-4e15cd621131 | -12.16865 | -38.37829 | 2026-08-28 16:05:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| db75948e-f958-393c-9e1d-0dc1211db155 | -13.33073 | -46.92504 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| fd4621a4-d2bf-3159-a5af-3af2fafbdbd5 | -17.29841 | -46.5796 | 2026-08-28 16:05:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8828d0cd-c14a-3904-863d-80ed7c519e39 | -8.96359 | -42.69935 | 2026-08-28 16:05:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 4e2c22ac-ddf5-3d3f-9f36-c16ad907e91e | -5.9639 | -44.80259 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 097d4728-9c8c-38e3-b808-762c83b2c807 | -7.48781 | -37.48128 | 2026-08-28 16:05:00 | NOAA-20 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d0df7e78-c4b5-3441-acd4-fc5bd6c7e2f7 | -9.63812 | -48.27208 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f1ccb285-2335-3433-a0b8-590c6d506a5c | -17.5751 | -46.51387 | 2026-08-28 16:05:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1cdd452-6c63-3944-be55-2d0f8824a8bd | -7.12018 | -43.16903 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 553f44a7-ae5c-3557-b0ea-d41415a06db9 | -8.17324 | -46.16647 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 971c0717-0ff7-367f-b4f8-a2d92e3cc1bc | -14.1783 | -48.76913 | 2026-08-28 16:05:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0b85dab6-ec82-37ae-a60b-846567c033a3 | -13.89265 | -39.84596 | 2026-08-28 16:05:00 | NOAA-20 | JITAÚNA | BAHIA | Brasil | 2918308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 51aad7f9-9ed2-3248-a9e6-31314a31860f | -6.89653 | -43.64091 | 2026-08-28 16:05:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 177b260e-2875-316f-a714-3b85f00f3bf3 | -13.25888 | -43.39571 | 2026-08-28 16:05:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 0ba59455-952d-3f12-a876-ef35623d4aae | -7.62107 | -44.81864 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 93ce1d8a-0f26-3593-9440-9404abddbf9a | -6.90184 | -43.64805 | 2026-08-28 16:05:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 6b8cc2d3-79ef-3bb4-8ca0-a946a05815a8 | -13.6586 | -47.74305 | 2026-08-28 16:05:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 1b1c9792-ea89-30c5-839b-8438d562c6c8 | -7.71621 | -43.92117 | 2026-08-28 16:05:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c97d0f08-43ef-3191-b1c6-cf2ddf4d8657 | -14.18484 | -48.76834 | 2026-08-28 16:05:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1e4db83f-f884-3572-a6e8-3a0727b98e63 | -13.75277 | -43.5036 | 2026-08-28 16:05:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 886dc71c-a26c-39e9-9a42-756946f92f2d | -8.48653 | -44.79189 | 2026-08-28 16:05:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab7f1a03-1a72-341a-aa74-4fc6be66d335 | -14.19849 | -45.27429 | 2026-08-28 16:05:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a57e9a7c-544f-394b-8f01-5f1fbc6d6f72 | -8.08262 | -45.84081 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0068a0e9-fa7b-318f-bc3e-d4d52e8e1ade | -8.08301 | -45.84375 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0a517010-9fbf-39fb-99a2-3deb594b5da6 | -13.33462 | -46.90781 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 693e75fc-5069-3719-b30b-a981b54a5b91 | -8.48187 | -44.79264 | 2026-08-28 16:05:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52a68739-e862-3f3a-9943-2413976a5381 | -12.86962 | -44.35938 | 2026-08-28 16:05:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 929cfb41-40f3-327d-9b85-e12b72286ffc | -6.8348 | -42.8563 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ab348cd1-9217-3863-879e-3aba20e56b47 | -12.78658 | -45.9501 | 2026-08-28 16:05:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 425afd46-72db-3128-8738-e202e6f1bf87 | -11.94552 | -41.32442 | 2026-08-28 16:05:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4cc040dc-1df6-3f30-bac4-be60a290ae71 | -8.09759 | -45.8386 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |


[Clique aqui para ver as próximas entradas](README92.md)
