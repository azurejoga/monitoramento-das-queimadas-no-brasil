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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6285b45-1700-3d96-a214-37c68b9c44bd | -7.47721 | -42.85295 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b1be16b4-ba10-3850-a4e9-e29be306abae | -3.09575 | -53.94891 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e9e22d1-8f91-379d-9412-2e5e90bd5020 | -3.79445 | -52.39228 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91479227-a101-34e4-b701-55fbd81c5eb4 | -10.86038 | -45.53846 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2987a05-a4c8-3dc0-b841-5485708e9e5b | -2.94269 | -54.18535 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73cc6a0d-8ad9-380b-be61-9ca9c8bd18cd | -11.25606 | -45.18011 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7b62934-9276-3b72-abe4-ba749818161c | -4.51549 | -54.89672 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3364e592-cbca-3a78-81a5-6386cadfa941 | -3.48163 | -54.73343 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97c784e9-815d-37b0-81a9-ee8f6db8ccc5 | -9.08218 | -45.11525 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acc161d9-4003-30aa-b6fe-3a2a53d12ae0 | -3.08282 | -58.09409 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 516ef01e-9cbb-3e66-b07c-8be10f13e501 | -8.43304 | -47.02687 | 2026-10-09 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9d2ebcb-bf5e-3123-878b-90127a153d7e | -6.72774 | -48.11893 | 2026-10-09 05:04:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 629ccfd0-2f2a-32d6-a1ed-c904e847ee13 | -5.9686 | -55.34246 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf7a59f3-241f-3b0d-b885-c588711b8b2b | -2.93087 | -54.08029 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9bbc02f2-1b90-3fd4-8058-721b2621ae2a | -4.52138 | -54.86087 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63c5e888-f69a-39cb-b1c3-48f65af6aba5 | -11.01108 | -45.42851 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 30073b45-3f4d-3095-af0c-2f0cbe25aaa9 | -6.11218 | -57.85753 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6888c56-b7ec-351a-99cf-188ccaf048f8 | -4.66515 | -56.21192 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6fc590a3-5930-3128-8cd4-06978b5223d0 | -2.86691 | -54.16154 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fbba392-d424-3ad5-bb24-b829b9829aaf | -3.26921 | -54.06087 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92d4ff81-0034-36f8-96cc-9d002e37d8c0 | -9.91064 | -44.78499 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffd2747b-be97-38d5-90f7-91aa44a370e6 | -3.00718 | -54.09642 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 146c59ac-34db-3cb8-b2fe-22a6b275e50b | -9.21068 | -57.72888 | 2026-10-09 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9936af68-4c28-3ca5-b961-f9a6b41ed772 | -7.3989 | -44.74847 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d5667bec-b8e1-3929-bdd2-e83a6cd9f804 | -5.61683 | -44.83706 | 2026-10-09 05:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9bf40f7-1db7-3aee-b22c-50063828dcae | -6.00544 | -40.9682 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| df8d0a33-c2c2-3978-a7c3-0601da0cf005 | -3.8681 | -55.98932 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54cfab38-6ffc-3f14-9301-d157a75e1295 | -4.80468 | -56.14098 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3949dc85-01aa-3b8d-ab99-aeb47f2eb7b2 | -5.19348 | -46.22147 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc8cb831-1be8-3923-ad3e-c0848e2d316f | -6.02384 | -51.72626 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19ff74c9-04c3-3f06-9477-43e2f5184644 | -2.89858 | -54.07522 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9abab82a-7f34-3f68-9f5e-372f848cb446 | -3.00548 | -54.08731 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbd910dc-2b2d-3876-a8eb-b6a963b8e43b | -4.3239 | -54.90154 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cc43725-c342-3f62-ab7d-5b5a8d73e8fe | -4.43036 | -55.16108 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d46407d7-6c0f-3ff9-b355-9d9fb20659c9 | -9.88848 | -50.48913 | 2026-10-09 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e65fef3-2c43-3e74-8d2d-865ea2d2382a | -5.98477 | -55.37848 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e697988-0eb6-31c2-ae1b-2b9ec9dd2cee | -2.58031 | -56.18426 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a22bfb8-2115-36ff-b78e-21b7af80d4c0 | -2.88587 | -54.18027 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c917e9b6-67da-36e2-baf2-abeb366c1135 | -2.89129 | -54.16917 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8885290-5b82-331c-9893-0434a74019a3 | -3.73687 | -59.4475 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f9f193e-9bed-31ae-bf10-4f71124b79c4 | -3.05775 | -53.9195 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7011a96b-f27e-3f4c-b399-d9b2dd0f461a | -4.98369 | -46.03922 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51505b4c-ebcd-3941-a025-50b16daaa2a1 | -8.23475 | -54.7362 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e42abfb1-55fc-3625-b090-47ef30b85ece | -3.89511 | -55.89411 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| daf1ee49-6b29-3462-938b-6b4f0cbfd0d0 | -5.23716 | -60.18856 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b65cf77-eee2-3919-9cf3-6393ad99a911 | -3.30336 | -53.69598 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38c60e44-1269-3257-917e-8d357301c341 | -6.09398 | -53.47968 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d53c53e7-f92b-37e5-afde-83aa38c63a91 | -6.51428 | -55.38152 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 695641aa-692a-3aa6-8ec4-7d96fc642a59 | -3.00333 | -53.8961 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 01591607-fc1a-30a7-b3ad-5de169a5c516 | -5.34184 | -45.1771 | 2026-10-09 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7dbecc53-49a3-31dc-837c-3432b9222aa7 | -3.0845 | -54.26684 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a434352b-a059-3bcd-bcf0-0208f6949c58 | -4.29242 | -54.81054 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6cb09a70-9340-3337-849f-8609b052d00e | -6.2426 | -52.86277 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8042dd19-9385-35ef-8af3-762c7a87f3c3 | -8.84669 | -61.46294 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9acf537-d9c8-34cd-a694-82096a28a41c | -3.66594 | -52.11305 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f59eb93-7825-3f60-bfd1-5bd8865f671f | -2.88398 | -54.19191 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49245376-a757-3309-b78a-e60c5cd1bfa5 | -8.32365 | -49.12498 | 2026-10-09 05:04:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa0cec39-c76c-331a-9ffa-e3ef97286102 | -9.87715 | -50.49167 | 2026-10-09 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91289c49-8e23-35c8-becd-59c41ad3f04c | -3.01085 | -54.07634 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d7bffcc-037c-33f2-9fc1-9a7cd86596c9 | -4.97933 | -46.03849 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13482d3f-b0a2-3b04-93ba-37092a7e84c4 | -3.94112 | -55.84789 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0508bbee-e138-3d12-814b-b98242a2cfa0 | -6.08595 | -62.51157 | 2026-10-09 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8984a36c-5546-3415-ad6b-a8deb1dacb0a | -4.57192 | -54.95525 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e27e0692-0e43-3947-9184-e42cc5595daa | -3.5385 | -59.40173 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea7c223f-128f-3001-b6fa-07ee0b77582a | -7.44022 | -63.55556 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86a2a57c-0132-3b52-aa1e-a3d83a108269 | -3.08941 | -53.94403 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 736b23f8-d1e7-3992-b3ec-11f975bd85d8 | -11.06976 | -44.08849 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf0ff6b0-9e5a-338d-bf15-a7c2078c6997 | -5.94935 | -55.34752 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f97c8c8-0bf9-3d53-87af-fb0b39073e5f | -3.17095 | -54.73685 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25653d61-16ed-35d5-8d7f-f32783027c45 | -3.64817 | -54.28414 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6246ff93-b36e-321a-907a-6934de0e3a16 | -8.32995 | -45.4548 | 2026-10-09 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7e825cb-915e-38ca-b7b2-f67beeb2b6ca | -7.96527 | -46.88586 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 543ef238-bf1f-39c7-89bd-5c7c8e7eafb4 | -2.87918 | -56.66275 | 2026-10-09 05:04:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88911b62-df02-320c-bc8e-95599b0a4b35 | -3.09571 | -54.28768 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84503f36-f690-3a53-b392-9016b968cdca | -11.00682 | -45.42217 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5309f407-7ec7-3e9c-addc-c136f88b5992 | -6.14544 | -51.94599 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41af785a-d320-36bf-a44d-8f936b9df8c2 | -2.8559 | -59.27323 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57385947-a218-39df-b9af-14b0823233c2 | -5.35302 | -43.40547 | 2026-10-09 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c18b26d-51c5-31a5-bdc5-8d75e6fb5566 | -8.49279 | -54.63335 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a7b851a-e226-3062-88f1-d64b3d267aa1 | -5.26232 | -50.14239 | 2026-10-09 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 087eba8e-f9c3-3032-ac1c-b980fc6fdc37 | -4.63349 | -50.95702 | 2026-10-09 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a1485ed-961a-35fb-9188-2d87494863e8 | -6.49647 | -55.31223 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 991cc815-373f-323d-886e-20c0325dd9a4 | -3.07881 | -53.96566 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90ac9b34-4523-3193-b4c3-fc989bcf6a1f | -6.24704 | -52.85634 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4467b68-374d-3478-b14a-f62dd0ffa261 | -3.57197 | -54.68444 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2561558b-3965-32aa-b7af-442ad5ad3196 | -4.7554 | -55.66117 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5191ad4f-a4eb-3b31-9b1c-a53ae07b12f5 | -2.93211 | -54.07259 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d44088b-da2f-37cb-9151-a31a1157af61 | -5.86669 | -57.7551 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ba52980-63e9-3ccc-9658-c0a066edf945 | -2.99518 | -53.90257 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61c03cfc-06c8-35a2-9de0-173a0067beea | -3.03197 | -54.2344 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9d998bb-02ab-320b-aeef-b74aba2e3578 | -11.06402 | -44.08333 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b215f5dc-3433-3ecf-9703-eb3e408cb429 | -8.23414 | -54.73991 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 881e85d4-eb56-3623-b4b7-c5896cf09b8f | -3.47806 | -59.50262 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9bd07ab-b1e8-3320-8c21-69eb4c68dbe2 | -6.50002 | -55.31284 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 399f4afc-2905-3402-b1ee-4ac6ae5f6260 | -11.00388 | -45.4097 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9db6acf9-5040-338f-9711-64d38734be4c | -3.31057 | -54.04792 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74ef6f83-b263-36fc-9ac9-e73e804683af | -9.83763 | -44.78389 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad355173-0c32-3ddc-bfa9-472e011a2b4c | -2.47388 | -58.07851 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1de69faf-20c1-339f-ac7c-f905a6bf19fc | -4.74208 | -55.67292 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9325a318-dfb9-3cbd-8de1-829ab2bb4860 | -11.86917 | -43.5657 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README134.md)
