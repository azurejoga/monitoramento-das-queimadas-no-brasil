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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b2e2401-aaf5-33c9-8d90-ee9fdf6acd82 | -19.1806 | -48.7946 | 2026-09-18 03:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 173.9 |
| be47e9d7-3ae0-300e-afe2-282abcadc9d8 | -9.7177 | -54.8162 | 2026-09-18 03:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| d67a2e2b-73bb-3467-9983-5927d23bb468 | -2.6125 | -54.7577 | 2026-09-18 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 2d3d73da-5518-31bb-a260-672c673bf474 | -19.1812 | -48.7717 | 2026-09-18 03:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 165.6 |
| ee6e4046-df2f-3211-81d6-9dd85bf7d4f9 | -19.2009 | -48.7904 | 2026-09-18 03:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7e11488c-9037-3ed2-b359-baab2a839e7b | -13.2252 | -42.3414 | 2026-09-18 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 713d915a-44ca-3e19-b050-0f6ad2f61a21 | -13.2446 | -42.3377 | 2026-09-18 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 133.9 |
| 83a5c87d-ed0e-3d94-ac57-e2c6876e03a0 | -12.3206 | -50.7394 | 2026-09-18 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c5b87b40-fd68-3c26-87d4-8e37cdd5d6fb | -9.7179 | -54.796 | 2026-09-18 03:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| a31e94f4-cd40-3683-8d90-d20966341165 | -8.8921 | -62.4297 | 2026-09-18 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4f9fbaed-3c12-3764-b1e9-6c143794ca96 | -13.2451 | -42.3133 | 2026-09-18 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 8f4b7d0f-7492-31fa-9b31-5471f312f76f | -11.6609 | -54.4478 | 2026-09-18 03:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 4ca68b83-aa0a-32cd-996d-c191c5935803 | -9.7177 | -54.8162 | 2026-09-18 03:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| b273a673-2a44-31aa-8679-1d9fbacdab24 | -19.2015 | -48.7675 | 2026-09-18 03:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ec863c0a-6538-3c23-966f-0a755b24e8b4 | -13.2257 | -42.317 | 2026-09-18 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 0596bdd6-a75b-396d-b777-44f3eacbf431 | -11.6798 | -54.446 | 2026-09-18 03:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 23cf18d4-55be-38a9-9cd6-7cf1324f0416 | -12.3015 | -50.7417 | 2026-09-18 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ae098b13-3484-356a-9608-862f2259e7f4 | -19.1806 | -48.7946 | 2026-09-18 03:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 9bd80773-2cf9-319a-b7fa-a20919b364a3 | -8.8922 | -62.4107 | 2026-09-18 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dab4ab22-5932-3a2b-8d44-4e1f105e22f2 | -2.6125 | -54.7577 | 2026-09-18 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| cbeda205-d5fb-3e7c-a2d5-eca3c8dd85fa | -9.699 | -54.8176 | 2026-09-18 03:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7a07b602-0485-3e8c-8ac6-67445cf348da | -8.9107 | -62.41 | 2026-09-18 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ce51a3b6-8f9e-305a-bcaf-025b2f5e0865 | -3.0465 | -51.3755 | 2026-09-18 03:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c65197f3-fe2d-3df3-ae47-b1e00e091d0c | -12.5497 | -50.7332 | 2026-09-18 03:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| fe0c75cc-f914-3dde-93a5-db532677acdb | -5.62498 | -40.85763 | 2026-09-18 03:36:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0286cf81-849f-3bd5-a610-c61b3cf9a738 | -8.44025 | -45.70673 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe617410-766a-35ea-8106-16303548f49b | -6.99509 | -42.16029 | 2026-09-18 03:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21b556c6-6761-32f9-b6a2-99d0bbf313ff | -4.56343 | -42.96122 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 58cb584d-8977-30e1-a987-3acbb1bcc39a | -8.45797 | -44.51328 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 102a53e9-52f6-3403-b8ea-e6e308c371a0 | -6.99721 | -43.63833 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| cb7f5ca3-71b2-3f51-adc3-6b17b0ffad82 | -7.34359 | -44.64097 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2da6c316-dc8b-3563-9e72-ecd5626dce2c | -7.79465 | -44.9101 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b7d5567-3893-3699-9832-8cb73634da43 | -7.04347 | -42.0816 | 2026-09-18 03:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9f87635-0677-3bec-902f-edbadbe3aa4a | -8.28604 | -45.62675 | 2026-09-18 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6fe3b0b3-9af9-3922-8b15-973f50d23f18 | -7.057 | -46.23267 | 2026-09-18 03:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 28809840-54c1-3e03-b6eb-2139e570b9b7 | -8.43595 | -45.70522 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 139a80ce-868b-34b6-902b-6d3b29ba3716 | -4.56668 | -42.94294 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4c3925d-a3c7-3026-a4a2-77c68a861995 | -7.34469 | -44.63526 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81bdf4b9-e061-337c-94cf-d2dd44677ee0 | -4.58246 | -42.95979 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8b9c4a17-74af-38ed-bf32-d0b9e593a877 | -8.48115 | -46.88521 | 2026-09-18 03:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1f4f3117-f686-3640-a822-47c9b334cb9c | -4.55553 | -42.96722 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fff3fd2-5612-36bf-901b-345a8c56f50e | -7.82222 | -44.90389 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59030a3d-bb97-3847-b593-dc8fbec5029a | -7.93574 | -44.8382 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64ac58d9-3cdb-340f-8142-faac63dcf6b1 | -4.5708 | -42.95108 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bd9cd4f4-a879-3203-a091-c11a75181a69 | -7.67186 | -46.11241 | 2026-09-18 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5778ca7e-5f05-3c47-8f30-5f8a4ea7d464 | -4.57003 | -42.9556 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bb2e4121-5ea7-3b04-9153-ed88f1e57f36 | -5.74978 | -45.09628 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9c0a32c8-3012-36eb-b940-dede3c6f013c | -6.27753 | -41.66619 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 45ad6f3b-ce6f-3816-92cb-307179df69dc | -7.0087 | -43.64342 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 38e659ab-b3e8-32ed-9f8e-3d2c9ccde936 | -4.56397 | -42.95449 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9e7c3123-97ff-3abd-ab1b-998d9e800f40 | -8.71099 | -44.88007 | 2026-09-18 03:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27decaab-188e-355f-af60-d626d5639ad9 | -4.57114 | -42.95304 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4c222c3f-3a24-3de9-ac7f-536836d8894a | -7.93584 | -44.83553 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcfc5835-9367-31a8-b6ed-6fad9f24b1a9 | -4.56844 | -42.96496 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 11f04791-3d82-397b-8403-e2b56f9708f0 | -8.29165 | -45.63373 | 2026-09-18 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a87bf8cf-f1e7-3bbe-9d33-6164d2bcb16a | -6.2829 | -41.79878 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf877641-22b2-37ca-a39f-5eb39f44ec36 | -6.40936 | -43.46881 | 2026-09-18 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9ab42e0-770a-31df-b9fd-8b3c69fe6ad3 | -7.83202 | -44.88802 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f084fee4-1410-3b07-8a18-237e5e0c4970 | -8.08201 | -37.6899 | 2026-09-18 03:36:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ae28650-913f-375f-951d-72c7a22298fb | -6.99652 | -43.64111 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6d406c5-4613-3fde-9a21-6212eb2fd991 | -7.29494 | -38.96136 | 2026-09-18 03:36:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 156fc42c-f1af-3833-9fcf-f8033ce6832a | -4.5764 | -42.95868 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ac01c55a-2220-32bb-a027-c4aee790c9fb | -6.45413 | -46.01998 | 2026-09-18 03:36:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb1fd7a8-11bf-3d83-8ab4-385aaaf03914 | -7.35045 | -38.98487 | 2026-09-18 03:36:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d17dc29a-604a-382f-b8e5-5016543180e2 | -4.55474 | -42.97183 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aeb97464-6b95-38dc-9c93-7956b970b95c | -4.57557 | -42.96336 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 847dcf1a-d7bf-3ab8-8777-bd3affdd9ff3 | -7.28972 | -38.96491 | 2026-09-18 03:36:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 10b9de04-fdd4-33df-87bc-b11b0aaeb1f2 | -7.0234 | -43.63163 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca6fed95-9d1d-3098-a8cf-c5cc421cf53b | -4.57722 | -42.95406 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6e32308e-485c-3846-8fd0-1fd10cc604d9 | -4.5582 | -42.95541 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e8a97b64-bf67-3ed8-93d1-3e24b49bcf10 | -6.11625 | -44.03646 | 2026-09-18 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58239ad0-0c3d-399c-85bf-08c2c5c0acb4 | -8.44414 | -45.8416 | 2026-09-18 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 969cc008-68f9-3e76-af2c-7d0e788432b0 | -7.80767 | -44.91241 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8e4ad0e5-7ede-35a5-9774-576b2fba36c7 | -4.55712 | -42.95797 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3be444c5-f2bc-3b2b-914b-3d279b8efb3c | -4.58851 | -42.961 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d7e256ac-056d-33cf-aeb5-31e35ade9c2b | -6.99575 | -42.15665 | 2026-09-18 03:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1d4edcf-2d88-35e1-a35a-325a6af69771 | -7.79364 | -44.87999 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f85fd45-37e2-32d9-8c9b-1b164d089856 | -6.28903 | -41.79614 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 81b1211f-217a-3e3b-acb6-bd67f5edaadd | -7.01723 | -43.63235 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3ad9b3ba-723d-37e1-be02-01924ab1d9bc | -6.29775 | -41.77898 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a7e33a33-3d99-34c4-9934-bef386aafcb5 | -6.9141 | -41.72191 | 2026-09-18 03:36:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| adb1256e-ba4a-3e0c-8468-63a0f635b0fa | -7.29617 | -38.96304 | 2026-09-18 03:36:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 51779d0b-3c88-31bf-a1d5-62e1ab61dfda | -4.58163 | -42.9645 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1fcff83d-d371-3301-aa05-e74fec156707 | -7.28732 | -38.96116 | 2026-09-18 03:36:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 04617c58-884b-3ece-90bd-261faae5d77f | -7.03729 | -42.08434 | 2026-09-18 03:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3294582f-b0fb-3825-b864-b858f7b0514c | -7.05342 | -46.23095 | 2026-09-18 03:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| efb2692e-f3eb-3cb2-a88c-189d29bfb238 | -5.62985 | -44.80888 | 2026-09-18 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 82c24c5c-3a5f-3ac3-90fe-a7ab8fb64d40 | -8.46662 | -44.53664 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 063d1420-d33a-3af9-9a8e-b0997b339a5e | -4.94121 | -42.89174 | 2026-09-18 03:36:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 195e8565-b396-3dcb-81b8-e6caf26a313a | -8.90613 | -45.01699 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bd340f88-cfad-31c0-b6fe-e7b9364a7252 | -8.53611 | -44.54755 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8fbad82-91ed-3080-84e2-a68da0b3c904 | -7.81455 | -44.90873 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b83b4133-2e42-35f2-833f-4b190f879b38 | -4.55185 | -42.95216 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3650ba3-6a27-382b-a3ee-60cc3fa349df | -8.94598 | -44.39733 | 2026-09-18 03:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ec691ea-4cfe-38f6-8adb-801ec967c0c5 | -5.33564 | -45.1455 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81d7d0ec-f05f-3f19-b59d-c5100efb4f0e | -5.61799 | -40.86698 | 2026-09-18 03:36:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e42c4db-85c9-381a-a0ef-8d2b4c86e2e6 | -4.56587 | -42.94751 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83e0f104-7847-3efc-ab03-1d4eba6b34f6 | -7.00003 | -42.16462 | 2026-09-18 03:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8cc4faff-bdd2-353e-b17e-4e32c1e97321 | -8.53513 | -44.55253 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf3a958e-21a9-3f6e-ae69-a6c1a6d14ee6 | -8.70343 | -44.89111 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README24.md)
