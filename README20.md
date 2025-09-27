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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cda5d45-7f4e-337d-8c24-9266e104cf96 | -11.2983 | -47.81614 | 2025-09-27 03:55:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b097cc4d-c83f-39da-ae33-6e6ac7c0f19e | -9.54927 | -47.77298 | 2025-09-27 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b52b7b9-cf63-3b3e-bdb7-0b60a0e18f23 | -7.67348 | -47.42113 | 2025-09-27 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcdd6f22-8ebe-3f26-a318-8a7cc48bb1a6 | -11.79004 | -44.9082 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a91203b0-62f2-3828-a8ee-e02f0a4bab39 | -7.87835 | -44.0167 | 2025-09-27 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ea6d9a8-fb6b-3e8a-9dcd-3daaa230c793 | -8.65688 | -43.99292 | 2025-09-27 03:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 80eb1373-9304-3784-ad0b-0af30eaf6577 | -9.00947 | -49.17092 | 2025-09-27 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3327540-b9e8-3990-9a8f-60da93384b87 | -11.97358 | -47.9101 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5f8a903b-5fbe-3b62-9f9d-e962f29479c1 | -12.83742 | -44.68793 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91275c8b-6f0c-38b1-8b65-2ef5823824fb | -13.87957 | -44.2426 | 2025-09-27 03:55:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2ee47e3-235b-3a20-b314-82db501d525c | -13.32699 | -47.30976 | 2025-09-27 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d3cd447d-a31a-37a0-a144-aaa2e39103e2 | -9.96806 | -43.60773 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8afa93c-782d-31bc-90ef-4f8da9f5cf88 | -13.43177 | -46.51718 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a79f42a9-4538-3db3-96ce-4aba5b76fbfb | -9.114 | -45.87231 | 2025-09-27 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ae6ba705-0c04-314d-ae80-18bee466b3b0 | -11.61242 | -48.58223 | 2025-09-27 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d42c83c7-8b43-3d4e-981b-1bd1625bf492 | -11.94567 | -47.86964 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a994aec0-795f-3fee-8b62-fc3939a1a6b2 | -6.70475 | -42.75325 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b2b537a0-0ba6-3057-85dd-7a9f9721bb8e | -11.53866 | -46.95187 | 2025-09-27 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6b62225-8984-334c-ac19-619d0b686bd6 | -9.9258 | -37.59601 | 2025-09-27 03:55:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2abbc72b-e47f-38a9-ab6c-2779defe0725 | -11.38704 | -44.93809 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3642fc0f-eb86-3dde-a064-278893e9ffe6 | -10.12526 | -45.33471 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34cdd4c3-42f2-329d-aa42-8e8129151d65 | -10.25548 | -50.23895 | 2025-09-27 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35f8f4b8-eb7c-3ee7-9754-2dde7df37f16 | -11.29677 | -47.81862 | 2025-09-27 03:55:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 01b55034-6285-34e8-9beb-d17195aa4667 | -8.52517 | -44.63283 | 2025-09-27 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0b69052-b74d-3a7e-8b73-50b9f68ee9a0 | -9.69476 | -48.93907 | 2025-09-27 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e87a2686-ef22-3904-9a44-b4c4a457420d | -11.97285 | -46.59766 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6aa3614-8fe4-3464-ba15-145cb7f0cdad | -11.37646 | -44.95068 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ae630b5c-479e-3d38-923e-e76601d79d83 | -8.83597 | -46.21772 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0da9032-b310-361b-8f32-7d46b8fc3c79 | -7.78366 | -46.93846 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00abf4de-e604-3550-bd33-c61765a36db9 | -7.0507 | -43.02807 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b6a2ec0-bb01-326a-84b0-a9d7baa696da | -11.40159 | -43.29943 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 973f9959-4829-3e9c-9651-47da120d5197 | -6.71168 | -42.73506 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6a73f69b-b40b-3b0e-9908-c44c3f251738 | -10.12452 | -45.33883 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 84a14ce1-be42-3b24-acd0-6990ff585e62 | -11.36349 | -45.00133 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4cd40fc-8e9a-3242-86e0-20f1d7e0d448 | -10.17909 | -46.93179 | 2025-09-27 03:55:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e76d6af3-b524-34c2-b57d-d9833847c997 | -6.54704 | -43.82711 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34f67321-b86f-34a7-a8e9-a699aaf2efaa | -10.5874 | -46.27552 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af1a515f-70cd-3fb6-9278-7f0a74462749 | -11.65585 | -45.3458 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70267344-6671-3ba8-a9c6-e951bc816d9e | -7.07236 | -43.85977 | 2025-09-27 03:55:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aae2da18-d93d-3b59-949b-7341dd8e5dbe | -11.43872 | -44.92843 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68223631-fadc-31b3-84ab-af2de6f89913 | -10.12573 | -45.33926 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ec11441-112c-3740-81fd-7314abb04def | -10.2417 | -43.94639 | 2025-09-27 03:55:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e74cd4b-aef9-3776-b387-e1ee27c1762d | -11.97958 | -47.90525 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 97bf3944-938f-356f-9b09-b047bc936499 | -6.54234 | -43.83002 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e45524b-fe22-3b15-8069-14f5e6fe2e8a | -7.62705 | -43.84445 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8760ae84-6657-3933-b122-93ad88ec0709 | -7.56881 | -42.41129 | 2025-09-27 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59c14f8b-8b62-3e61-ac97-1f1efbf4b073 | -7.26688 | -42.97742 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 98a8c28a-2f27-3e67-9a1d-fc632b900c13 | -6.55274 | -43.84357 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3647a67b-ea79-38a2-ab08-6f1e0461e2da | -7.04488 | -43.0298 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8b03a57a-0747-374f-bb02-26b443c5e33c | -9.69352 | -48.94255 | 2025-09-27 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8025c963-b715-36eb-a9d1-c77280116b2a | -6.94811 | -43.25289 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b7206319-35fb-3878-8d81-53f89ee5fe1a | -8.81893 | -46.25995 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c2f2e63-c2cd-3838-a6b7-d2cd722d671b | -10.60399 | -49.64186 | 2025-09-27 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3d5f58f3-52b4-3fcb-9e57-0dff8ad82d38 | -11.6154 | -44.40386 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e7a447b-7fc6-3f44-a252-f5af0c739cb1 | -9.98216 | -43.57068 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa1979a9-6f63-3983-8bd5-baebc58f8149 | -6.69854 | -44.57967 | 2025-09-27 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58c9b24d-dc3a-3262-9199-84440fc8a8b5 | -12.83261 | -44.69236 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 834706ce-8420-365f-91f2-418b866675cc | -12.98335 | -49.43415 | 2025-09-27 03:55:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be8de67a-3028-39db-9aab-0b5212241a74 | -9.87787 | -45.90705 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3949ffab-bfea-3acf-b7ab-886129de8a64 | -12.06696 | -46.62734 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5795a4ed-fde9-3991-948c-c9d79f8b15b4 | -11.69077 | -44.45641 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4f0d053-26a1-3485-bbc2-821366cd5863 | -7.94096 | -45.19892 | 2025-09-27 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58e76a80-b838-3bf7-91c0-1cc0fedfc7a5 | -11.97739 | -46.59831 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41f0f89d-0609-360e-9af4-75abe754119e | -11.6957 | -44.40751 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc7e2c47-0edd-38cb-a349-1b9abddc81e2 | -12.28484 | -44.05304 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ec43744-58fa-3fff-a4e8-248a57a30608 | -9.89349 | -49.12277 | 2025-09-27 03:55:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| af3e4c96-ad35-39e1-a4ec-ec13f6a8131e | -7.05152 | -43.02322 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a0fdc67-f318-3266-a638-c79e56741471 | -7.72033 | -47.30382 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27bac0fa-cd73-3012-8585-fa35bac14f0d | -6.53759 | -43.83323 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0da601f2-671a-3612-bf32-9eaee98d207b | -9.54981 | -47.76999 | 2025-09-27 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b1ce185-e673-33da-8ce0-9a576f86f357 | -11.37517 | -44.95814 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 48bc07d1-2cc0-3506-a2e4-dfcfa94fc815 | -9.08156 | -48.02245 | 2025-09-27 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63f545d7-26cf-3f5c-b8dc-579c1a5df399 | -6.70289 | -44.58006 | 2025-09-27 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 584d573a-6670-3c07-befc-c136a935cbeb | -6.99326 | -42.39387 | 2025-09-27 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ef08e8ec-1014-32bd-b1c0-6263a88eac6d | -7.34988 | -42.0959 | 2025-09-27 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 12fd2f9f-8656-3212-9aa3-f45b4bcea6fd | -6.4957 | -43.2836 | 2025-09-27 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa8d8205-4e83-347b-b6f3-6f8613b842eb | -7.34622 | -42.09531 | 2025-09-27 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2ea41e9b-f248-3ab7-937d-d884e0468f32 | -9.05064 | -45.51051 | 2025-09-27 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b07ea314-615e-36b7-97fb-bd4cd4437cfd | -10.61827 | -45.02918 | 2025-09-27 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b544a6d-aef7-35f6-bfdc-a1338f8227a4 | -11.24516 | -45.55499 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 80d1fc63-7a87-3d7f-a217-999b84a54c09 | -13.37425 | -47.82638 | 2025-09-27 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0db3a4e0-a8d7-34ad-bff4-9c04928fdbf3 | -7.71735 | -47.30924 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 581683f2-f967-3a6c-b3f2-8140de5541f2 | -8.18298 | -42.37275 | 2025-09-27 03:55:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0844dfd3-4dd9-3ebc-8119-60da9011a4c6 | -11.71555 | -44.40805 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 179532ec-298e-3cb7-b939-10464b78205d | -8.90967 | -46.09386 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9febafdc-13ae-34a9-bdff-fdf410c33234 | -11.71465 | -44.41315 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d645fae7-1471-3ad8-9be5-84813a5a5097 | -12.54721 | -45.84668 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e26bdc59-6bb5-3659-850e-bbbf88dc5425 | -11.6957 | -44.45502 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bbf48b9-0a88-3981-b652-1e6b1d0cf270 | -12.06572 | -46.62457 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e77e02a8-e8d1-386a-aaa2-1acc66cc67ea | -11.3017 | -47.81961 | 2025-09-27 03:55:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb0ce803-0bcf-316f-a30e-cd862b038d26 | -12.06488 | -46.62922 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7e015fa-0f61-3d49-8962-4d3c6a98da6d | -12.54277 | -45.85092 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f152272d-c47a-31bf-a1a4-9fcc556cbd0f | -7.00569 | -46.99654 | 2025-09-27 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5ee63b3-2a97-3201-a2d2-7098430f2843 | -12.95606 | -48.91045 | 2025-09-27 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 781ec3ef-542f-327c-819f-c059004f6c1b | -10.25464 | -50.24329 | 2025-09-27 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1a1b5f8-52a8-3e30-9dc0-96dbbf3970d0 | -10.16927 | -49.37838 | 2025-09-27 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 943941fd-1bfe-3e77-ad69-3c453b9b4134 | -11.38247 | -45.03156 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ac9f420-d6bd-3fc5-9119-3529275a34ec | -11.35679 | -45.01556 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53850445-6cb4-3335-ae97-d70a01c7160c | -11.43508 | -44.97301 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6e859e5-4aef-397a-af22-a4e14128bff8 | -13.06719 | -48.72055 | 2025-09-27 03:55:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README21.md)
