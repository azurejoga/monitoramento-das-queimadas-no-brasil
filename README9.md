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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db23d593-b8af-3a13-8e00-e592384a91c8 | -7.51374 | -42.15325 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| abbc70cd-0078-34d4-ba61-310e59cc4185 | -6.20721 | -42.67838 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5283328e-cb40-3d81-8fa6-96cde537e774 | -6.24091 | -43.01053 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d268cc42-6a46-3afc-896f-265ed05012f7 | -4.67431 | -43.12438 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a580ad3c-09b3-3f6e-b8b7-2ea804676a87 | -7.49465 | -42.15466 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 17f6516b-5756-3933-bb3e-a407a5e312c9 | -5.56166 | -41.32223 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8aa6f200-d882-3393-97cd-0d9cb0957d7c | -4.54904 | -44.0023 | 2025-10-13 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a98d07a1-cd41-3cf2-bd8a-29eae5ca345c | -6.56419 | -43.93003 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd78c9f6-8cb0-3be7-914a-d55a3d8a3251 | -4.52241 | -37.79228 | 2025-10-13 03:53:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4fc17c94-a8a7-368b-895f-1fd5cc8b0b33 | -6.77072 | -42.8358 | 2025-10-13 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e281aa3c-d015-3177-a978-7213c21db410 | -4.47857 | -44.92953 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8ac1793-6ff1-3d80-a2c1-a70f9086aae4 | -4.48637 | -44.93807 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1bb76c57-328f-3dbe-9317-86ffe6fd68d2 | -4.88925 | -41.55772 | 2025-10-13 03:53:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f58076eb-c65e-35e8-b8a5-6a5290803622 | -5.06628 | -40.47312 | 2025-10-13 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 29a474c4-3fe4-3b69-8db8-0d509424e756 | -3.58456 | -47.28154 | 2025-10-13 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7cd3c6fa-9121-3cbd-85d6-67f8032b10e6 | -2.24757 | -47.87715 | 2025-10-13 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4f34bd65-88f5-36d4-8e72-be7cbe6ddab9 | -5.45643 | -43.40047 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7307de4d-cf20-3e05-aea8-da7e083b155e | -6.17185 | -42.54193 | 2025-10-13 03:53:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| e993c44d-f56f-3394-bd7a-1ad09b506e92 | -3.13021 | -50.21128 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c4b6fd17-83bf-39c5-8216-103007ec7575 | -5.56527 | -41.32275 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 973db2eb-6065-3821-9e5e-7e28cb0d194c | -7.49727 | -43.0698 | 2025-10-13 03:53:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 83616bf4-0a97-3845-a452-0c414aa58245 | -4.47625 | -44.94382 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fd244e7d-5ba4-360d-b492-4ce13198f1bd | -3.13926 | -50.21156 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6347645b-43e8-3ae2-b43b-a6bb0bacf2c8 | -6.45098 | -44.24297 | 2025-10-13 03:53:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5ba9eff-65e8-36b3-8546-bbf8795604f2 | -5.81036 | -44.04825 | 2025-10-13 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb306e16-d3f3-3d1b-82c6-87f28ff364be | -4.47256 | -44.93582 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5c7111b7-547f-3a69-a6b1-b9808a52b6d3 | -7.49904 | -42.15089 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2903af18-006a-3a7c-9b25-e2521f27a613 | -2.53474 | -47.80051 | 2025-10-13 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| f01f0899-d14c-33ed-82fd-668d68c97b24 | -6.7613 | -44.64724 | 2025-10-13 03:53:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f3720ef-4132-3e34-bc6b-c26793beb018 | -7.06313 | -37.69248 | 2025-10-13 03:53:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2f9f399b-fc09-323c-87e6-309818b25687 | -5.81024 | -44.04754 | 2025-10-13 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f4ba106-eb9b-3aab-a30f-a3cc279d94af | -6.77232 | -42.83872 | 2025-10-13 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4977bf3f-753b-3560-900a-710728bfdfa9 | -5.04239 | -49.88593 | 2025-10-13 03:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04bd177f-5bd1-36c9-ae15-eea62eca425d | -2.529 | -47.79945 | 2025-10-13 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 33f093fd-1ece-30e4-b716-a5af3dd24e8a | -7.37567 | -44.07327 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f35f2ac0-3658-3ee7-bbf4-e9a5b67d7d0d | -5.04871 | -49.887 | 2025-10-13 03:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb2d37f4-114a-3fa1-95dd-748b9edb8ef1 | -5.91767 | -45.42889 | 2025-10-13 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 340de70d-a601-3768-9ce6-08ecc1800cec | -5.9385 | -44.21587 | 2025-10-13 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| ad594166-e775-32e0-9600-8780ec1b99f6 | -5.8605 | -43.85436 | 2025-10-13 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 514ef686-0f5e-3b75-92f8-46e3ecfda85a | -6.82082 | -44.64707 | 2025-10-13 03:53:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c55538a6-2b35-3ad7-9a04-4ccee91b79b9 | -5.90646 | -38.47555 | 2025-10-13 03:53:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4bfd22d7-55a2-3a83-8bf3-f9d44fe21253 | -7.64761 | -42.57088 | 2025-10-13 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1839944a-fa5d-36c2-ad83-8dddde37dabe | -2.54048 | -47.80163 | 2025-10-13 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cdccf179-b707-311e-9e76-525085a40d62 | -6.74924 | -42.16927 | 2025-10-13 03:53:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 741780d9-c030-3fee-b83a-236932a15c40 | -5.42406 | -41.33934 | 2025-10-13 03:53:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8e1d1c9c-d245-38ec-86e0-fe478d685da3 | -5.2187 | -50.95428 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 520e3f21-6177-3711-a0f8-0fa5b4974af2 | -6.20417 | -42.67282 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b5cecbbe-7725-39b9-8c76-fd77d6309993 | -3.58397 | -47.28505 | 2025-10-13 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0235ac7d-2bf5-3f2d-86f9-817f48a57f03 | -4.67836 | -43.12506 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c0514ca5-c114-3242-aa9f-8052d1ba3281 | -5.62993 | -42.68663 | 2025-10-13 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0ff926cb-be35-339e-af29-0b899e3656c1 | -6.27508 | -42.97468 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd934e22-cc72-34b0-9b2e-afdd60d57f2a | -3.47584 | -42.55669 | 2025-10-13 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bee413ea-fe0f-30ce-93b7-b91b5510c381 | -7.34768 | -44.08754 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6964578c-d465-3907-81a7-a7ee725cf561 | -4.0152 | -47.3513 | 2025-10-13 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41b9e223-88e9-3bcf-8435-617cfef5b0d6 | -5.31054 | -43.42208 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ae429871-36b6-3f57-8912-a6ccbabbe9e3 | -6.59116 | -44.08465 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 260d9671-c40b-3273-b530-19956b811775 | -5.29194 | -41.03675 | 2025-10-13 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 19ec9d72-f5c8-32a9-a509-264e20d4f59a | -7.50935 | -42.15701 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 92c29dd1-1ac8-352b-8b7d-2a3c4f7210f3 | -7.06051 | -44.26355 | 2025-10-13 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5972647b-e8dc-33f0-95b4-e4379e3a291c | -5.48027 | -44.65537 | 2025-10-13 03:53:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8c704ff-f5b9-33cb-a474-3339fdc22afa | -5.38828 | -47.20746 | 2025-10-13 03:53:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54b989c4-afa4-30d2-9e33-3f3fdff8be8f | -7.69347 | -41.47285 | 2025-10-13 03:53:00 | NOAA-21 | VERA MENDES | PIAUÍ | Brasil | 2211506 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a583f69d-1d77-3113-a5b1-f190ccd5f3de | -4.47555 | -44.94603 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 53921943-868f-37d2-a78d-e54dd47e9824 | -5.27387 | -43.39387 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2bb020fe-0fa0-3574-b201-fc034f512545 | -4.67776 | -43.12866 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 96e719b1-7487-3b16-88f2-484628db3dce | -4.47474 | -44.95081 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8447c2a-acf7-31a7-9205-46c41742e60f | -4.83748 | -41.48255 | 2025-10-13 03:53:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d4411e3a-b688-3875-b78c-b682aa1b0912 | -7.35531 | -44.09277 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0aec09ea-5db3-3905-9a8e-e00ec445ef77 | -6.97394 | -38.65644 | 2025-10-13 03:53:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ec726608-229b-3131-9025-c1118be2f622 | -3.13259 | -50.21063 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 675761ff-46b2-3a57-b027-596908bc47ae | -4.47095 | -44.94526 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c0f4ae63-6c53-34a7-a48c-adbc7c13e1c7 | -6.57311 | -43.92767 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae003b7c-ac11-3c16-a89a-6d84d6727f1f | -6.42469 | -43.58668 | 2025-10-13 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da23d59e-8565-3fde-aca4-1cf5b185daff | -4.53737 | -42.88754 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a27e2d64-b2f6-3ef2-9c86-fdb445659abd | -6.23213 | -43.01468 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dd8ecd3f-06ec-387a-8114-f40e0c8bb07a | -7.43685 | -42.97149 | 2025-10-13 03:53:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f48f2548-c80c-30df-aeae-6bdf7900bbe9 | -4.47397 | -44.92879 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68b1a2e1-2b23-3b93-8cbb-21c58c609ee2 | -4.4824 | -44.93505 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9d83005d-0d1e-38c3-b098-37c403cbbe8d | -5.91512 | -45.43562 | 2025-10-13 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb674490-4f97-3365-a705-df7382bf96b3 | -7.64309 | -42.57492 | 2025-10-13 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c79f1c61-683f-3e94-9cd5-7ae01b6e7fec | -5.45761 | -43.39321 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a4e7d3ff-1ea4-3f0a-80d6-a64d090b42b0 | -5.28838 | -41.03621 | 2025-10-13 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c9a7c23e-4ee1-382c-8c96-fa6c990471b7 | -7.40355 | -41.82046 | 2025-10-13 03:53:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 259a3310-d54b-3ca0-aaa5-b3d7ae9d35db | -7.4969 | -42.16395 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0b4b425c-97fa-36d8-8e4f-f72499da3686 | -6.63302 | -44.6575 | 2025-10-13 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f585ed71-01c1-3eb6-904c-8cd9189aa003 | -2.90894 | -49.1754 | 2025-10-13 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9788594b-ad96-34b2-ae95-70352d0e0ce8 | -5.83396 | -42.30103 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c9140b80-0c38-3656-ad8a-a5357666af3d | -6.40962 | -41.94722 | 2025-10-13 03:53:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d8832860-5bc3-3d50-a7fb-ca112ad9b565 | -3.34738 | -42.15932 | 2025-10-13 03:53:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e8682d3b-0ad8-3d04-9912-4ecb88d24fc0 | -4.01578 | -47.34784 | 2025-10-13 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e7bc1e6-ec93-30da-8777-922e34e91745 | -7.17242 | -40.133 | 2025-10-13 03:53:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| defe19f0-55e4-3436-a43b-1d1cb0190605 | -6.77167 | -42.81833 | 2025-10-13 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 86141dc6-3ccf-32c9-92cd-c1a602d4c3d6 | -4.47338 | -44.93104 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f9622b6b-9156-3876-996a-ea7a8b28ae12 | -6.56895 | -43.92704 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be7d6574-da28-3537-b96f-ee701a5a9660 | -2.26382 | -47.85047 | 2025-10-13 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7476c5e-1626-317c-8811-51f9fb4cccc4 | -5.04576 | -49.88686 | 2025-10-13 03:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5814588c-bb20-35c5-afd8-e94432f287b2 | -5.13118 | -42.87975 | 2025-10-13 03:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e7286a9-2bd1-370c-976d-6cb2f0eaf808 | -5.83243 | -42.31038 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c8372cea-713a-3854-a566-49266779daab | -4.48163 | -44.9398 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0f38b288-6acc-3d5e-9b0d-53fc35a9ed12 | -2.5334 | -47.80857 | 2025-10-13 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |


[Clique aqui para ver as próximas entradas](README10.md)
