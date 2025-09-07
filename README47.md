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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 131a191c-492d-3281-b504-f6fac3c29e0b | -11.77912 | -47.55819 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6fa8f10-146e-3760-8c35-1169084b7a54 | -6.87432 | -45.54642 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c257cdc-a469-3284-a651-3cba91a46983 | -11.4061 | -43.62632 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5dd3b5f6-2fb9-3f09-920a-e611b7f1e079 | -7.41033 | -44.9731 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51c0f1ff-9b61-3490-9645-d5cdbc1ea55d | -10.34352 | -44.90966 | 2025-09-07 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b269abdd-f700-346d-9097-470b843e302a | -6.59766 | -43.96251 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43408e97-33ea-3da1-91cd-2c50dc488198 | -10.06024 | -48.06289 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51c166fb-f53e-35f5-b07c-eff8bd114d35 | -6.21703 | -42.45781 | 2025-09-07 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| cd385577-1fa5-3019-856b-da4f0cc3185b | -8.45763 | -45.02948 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e9ee483-3dc1-3d16-9e56-48a70d5418d8 | -6.20892 | -43.36653 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daf50e5a-904d-3c3f-b6c3-9af2f047753f | -6.21229 | -43.41099 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efc53dfb-3812-3646-9d55-a74036627088 | -7.19784 | -44.72665 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 957844f2-de73-3b2d-87bc-3376b39ed999 | -8.08046 | -45.48245 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a4c7fe1-842d-3acf-ba0f-8842ac28a253 | -8.68321 | -54.66706 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8a097fe-3539-3e8d-a4f1-8333c0c7d5bc | -7.05823 | -52.71822 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9b66524-fe3a-33fd-b6b7-1353d5091c4c | -7.71281 | -44.7122 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64a6314d-8db0-3d03-b64b-0d400943e56c | -10.7361 | -48.59549 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a66abbfb-9b4c-3248-bcc9-ddd198a5003e | -6.06427 | -43.33331 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a3baa364-22ce-31c5-8f34-33cc6002eb8f | -10.60485 | -44.34082 | 2025-09-07 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 32535c51-62ed-3244-ba10-d31a9a1bed27 | -11.58475 | -47.17369 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c9036ae-4cf1-3580-8c7b-eb7d627c39ef | -11.30951 | -46.53627 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5de340f9-4add-3034-8e97-d98ed1702e74 | -5.58436 | -51.91536 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b89f8845-6b9c-3c6e-be5e-95ec53a503b1 | -8.04107 | -44.06766 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43c87e0c-d4de-380a-a2f3-e3573629e11c | -6.83956 | -52.85135 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ee060c1-18b3-350e-aeaf-990fef2793b5 | -9.41638 | -46.77115 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9649b371-3700-336f-98a3-aa216e09b052 | -9.98204 | -51.65828 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5d168f01-bdbb-3dc4-8036-e65e365a2c0b | -10.08216 | -48.0825 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aa76d8e-4186-35dc-adc9-11a98fa09771 | -6.21117 | -43.3742 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a2784e5-7cf1-3ef7-b4a3-89bf55bda5cf | -6.54338 | -42.93062 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d39693fc-d7f8-3aaf-ab6d-edebb9e6e7bc | -6.15143 | -43.18109 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b2f8a638-39ba-3e4e-a711-7883beda1781 | -7.60846 | -44.66372 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63a59e73-85ca-3310-8cf2-222dc230d479 | -11.01782 | -52.03929 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb39a1f8-c2dd-364c-8305-c373cd8aacb2 | -12.81536 | -48.02081 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bc4e674-1e46-3599-86c3-97649a28a26b | -9.97576 | -51.65855 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3d4fb85-fe55-382f-b728-615f4a8adee1 | -6.17112 | -43.18788 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e43850f3-e233-3135-afb8-e4ad4d004c63 | -7.21712 | -43.9944 | 2025-09-07 04:19:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d309800-117e-3f74-ae79-716e569f5d0c | -8.30236 | -44.98021 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a80de251-6fa5-39ef-a96a-8ae466ba8e78 | -7.60736 | -44.67068 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bfd937ea-e5c5-3957-b7d5-38c9abdae03d | -6.23219 | -42.65234 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c4a2f310-4f07-3b9d-9df3-fad6122eb50c | -7.0281 | -43.23995 | 2025-09-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 55bedace-bc11-31a6-a502-4910d745c879 | -7.74849 | -48.83011 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fec80c4-9bd6-33c0-a1ee-4f504f5d92ec | -7.75128 | -44.01239 | 2025-09-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94386382-4ac9-3578-8691-2311aecacd70 | -11.60963 | -47.15881 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 445695d1-baf4-3600-8180-5a03a67c56bc | -7.75184 | -44.00885 | 2025-09-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69e661f4-b03f-3f7a-a591-361768513981 | -9.74876 | -51.06586 | 2025-09-07 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d69d4e0d-9e2f-3e88-89ea-7a51f667fb37 | -8.45796 | -47.3352 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 936761da-1cb3-3c86-bbfd-0158c93ef9b8 | -4.89401 | -49.92781 | 2025-09-07 04:19:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4167f675-3ae6-3a65-86a9-82265e2cc91c | -6.52044 | -44.71501 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f05b62f-36de-3b3a-beac-53e4034839c8 | -8.44054 | -45.03032 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cd44887-9d26-3a89-86b8-eb3c723829c6 | -11.59717 | -47.16084 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 036b1341-db3b-3c5f-822e-65d15c9e0e80 | -7.53729 | -42.52535 | 2025-09-07 04:19:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 88e08d2d-d3e4-3aed-bada-f4ebd5468680 | -6.8001 | -47.07298 | 2025-09-07 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2277ec5-252e-35ff-8f7a-195b811e0920 | -7.03038 | -43.24773 | 2025-09-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 868f3874-2bae-33c2-91d4-a60d0820d5ea | -12.82686 | -48.01478 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e73c507-b8a1-3b57-baf4-f005e714be7a | -6.00726 | -44.15522 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c67a20d-ec1b-3993-9322-46af78e87f2d | -9.98347 | -51.65028 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73deaad6-5a73-35cf-9f86-4a03b9855f9a | -6.19866 | -43.57995 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d1bbb86-db09-3743-b2cd-db5822d690dd | -11.09455 | -52.06168 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c623894b-2760-30ce-a075-2e4999e6dbc9 | -6.15056 | -44.25972 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 623fb47b-9a9e-3c8f-a045-c5735f555706 | -6.83625 | -46.39445 | 2025-09-07 04:19:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b0e0eeb-b855-385f-af9d-5d17cd21bcaa | -7.81101 | -45.42443 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9459e70-4bd7-300e-aa7a-ec1439264712 | -8.14152 | -44.87966 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aa6e8d1f-9232-3e87-9719-52b602d918c4 | -6.48619 | -44.00201 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2a7dc679-f46a-3722-a7fd-eafcd2b72bc7 | -8.30739 | -55.09967 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6a89275-bb11-3b51-8193-068455c471a8 | -8.50356 | -45.10439 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 527301dc-d06e-3439-a370-e61f878f21aa | -12.22239 | -43.87295 | 2025-09-07 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c7a7828-8152-38e0-b6c6-8c9421df3c48 | -9.70975 | -49.49092 | 2025-09-07 04:19:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea6223c9-a344-3091-b431-a4259fc9084f | -6.23191 | -43.30763 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d269ca2-f6d9-3a1b-b4f3-ef92a3e947be | -9.7462 | -48.97225 | 2025-09-07 04:19:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a19707bc-a65d-3df6-abba-0b2b3bf440bd | -11.10976 | -52.0331 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e92ea1ca-5870-383f-a713-e75edabddeb6 | -6.21427 | -43.58971 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8532693c-8a9c-3789-81cc-a415a4f06a74 | -10.42999 | -42.53592 | 2025-09-07 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 48f70e76-d645-37bb-874b-3f31c61c5908 | -12.8194 | -48.01752 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d8a9ee9-a3dd-3b2f-a28a-1d4cddd49f8b | -6.91429 | -45.21021 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4fdb0a5-e776-3bc6-bcaf-355abab915e6 | -10.77325 | -48.26682 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e6cff7a-40c8-3d92-8bac-990b68a177c0 | -7.19675 | -44.73358 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1933e75-8a1a-3de4-bb46-50f84bfb20e7 | -11.5739 | -47.73878 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 470ee961-3118-3859-a971-f1d916dcf949 | -10.38238 | -44.9664 | 2025-09-07 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1585d206-383f-3063-93bb-3ac82a96f809 | -6.28201 | -53.4339 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 243bedc6-ed16-3013-ab9b-19e07fce5030 | -13.18738 | -44.48335 | 2025-09-07 04:19:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c90bc9c5-1f2a-35a6-b0cc-3ba7f638e314 | -8.14978 | -44.87027 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dfdcb59-8991-36d6-9eee-0b6f9fc61f67 | -11.01658 | -47.95152 | 2025-09-07 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ef313ad-7f5b-343c-8945-bdde1c1a17f9 | -6.19306 | -53.26316 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5303e51-b3eb-3b49-a1e8-8a1b35f86d81 | -11.41127 | -43.61531 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49abe98f-a85f-3f61-813c-417d11839940 | -6.20389 | -43.37674 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 549fdee3-aaa3-310c-8a1c-a6df0c4dc8e5 | -12.73515 | -45.11134 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 918d32e6-ce07-38a3-a5a4-c7a14139cba9 | -9.81451 | -46.82812 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3787265a-2300-3b01-8ff4-a805eeecd1db | -8.62255 | -54.65166 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b7f9e13-0fa7-34f0-85e6-1f6a2ce77338 | -9.98775 | -51.65117 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c55334a-e216-3902-8a6c-d6a9ef8fb84c | -6.16598 | -44.24797 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9eea1c0-a20a-3a0e-b676-c6608f54471a | -6.10806 | -44.76663 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 656fdf00-69ee-38de-b14b-f137521b66e1 | -11.61358 | -47.15571 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 77ab9562-f177-3bfd-8227-aaeb1096c9dc | -6.88145 | -45.58718 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a6cf782-65d0-3f12-ad0e-cd0df0a41bcc | -10.7866 | -48.27316 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65a3c7f5-aabc-321d-9174-e9d5863ed552 | -7.4351 | -44.94506 | 2025-09-07 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d9bdefb-0f8f-3129-ac36-182cd1447c04 | -11.28605 | -41.99634 | 2025-09-07 04:19:00 | NOAA-20 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8586f057-8c33-3ffa-9303-3dbafaa8d1fb | -10.32829 | -52.56177 | 2025-09-07 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5bd1c31-e6a0-3796-b2cb-fbe1c02f23cb | -8.04049 | -44.0494 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20724c09-f7f2-3fe6-95f6-e4bef987590e | -10.72401 | -48.58049 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe57d2db-183c-3073-b946-79668789f98e | -6.25147 | -43.50462 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README48.md)
