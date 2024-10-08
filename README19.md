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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c60ef49-d987-3843-8a9d-f4bfd1b774c7 | -6.6649 | -47.103901 | 2024-10-08 01:01:45 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9475f6c5-2790-35c3-a675-54325128c7c1 | -5.8254 | -44.114201 | 2024-10-08 01:01:47 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3106369-6127-3f78-809d-8088729aedad | -5.8116 | -44.100101 | 2024-10-08 01:01:47 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d091eb44-28ed-3875-b66f-c43af5127c8d | -5.8157 | -44.1166 | 2024-10-08 01:01:47 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ec1ff22-fcb2-398f-a27e-fb49d4ebf456 | -5.8198 | -44.133099 | 2024-10-08 01:01:47 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cebb84af-89c6-3ae0-8688-bff4e660e993 | -5.9201 | -45.384701 | 2024-10-08 01:01:51 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e717433e-08da-3162-8f7b-629d2c6e7362 | -5.9233 | -45.398201 | 2024-10-08 01:01:51 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4ff14a6-fd6c-38e3-8a5d-7c90007e1d0e | -5.9104 | -45.3871 | 2024-10-08 01:01:51 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0edaf31f-900d-30eb-b1d6-de9a73de9a10 | -5.1398 | -42.875301 | 2024-10-08 01:01:53 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14025bb6-56b2-3c45-9954-2bbf73d974cd | -6.0483 | -46.597198 | 2024-10-08 01:01:53 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ea85994-7cf2-31ae-a6ec-5b79b818d4d8 | -5.5749 | -44.8545 | 2024-10-08 01:01:54 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0742b35d-babc-37f2-96a7-bd550f718dc2 | -5.5785 | -44.869301 | 2024-10-08 01:01:54 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63e67fe4-878a-34c4-976f-49537f3af5a0 | -5.5821 | -44.884102 | 2024-10-08 01:01:54 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 340abfc2-33ec-35d0-b04f-e8b371742908 | -5.5651 | -44.8568 | 2024-10-08 01:01:54 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83d210a9-c202-3b95-8da9-967645dda99d | -5.5687 | -44.871601 | 2024-10-08 01:01:54 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f1c9dda-d6ae-3c21-a78c-94daa1685f53 | -5.5723 | -44.886398 | 2024-10-08 01:01:54 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61f5f9ea-38c5-3d4d-b881-754cb03b4f8a | -5.7166 | -46.4603 | 2024-10-08 01:01:58 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f6910e1-f349-33ae-92a4-06bdc1e02b5c | -4.4564 | -42.887402 | 2024-10-08 01:02:04 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1b9045f-e4cd-36e8-bac0-c49da9815c51 | -4.4467 | -42.889801 | 2024-10-08 01:02:05 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efbff7c1-0483-3f5c-9333-3869aef975e4 | -4.4519 | -42.9109 | 2024-10-08 01:02:05 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 455fb77e-c44b-3127-8e8f-767cb374bd88 | -5.7489 | -49.2467 | 2024-10-08 01:02:08 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 879d7828-634e-3d7b-95fe-59b52d92022c | -4.925 | -46.768101 | 2024-10-08 01:02:12 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01617ca9-e6df-34f0-aa15-b74df1ced272 | -4.2707 | -46.2705 | 2024-10-08 01:02:21 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ee765ec-3360-3b7b-bab3-636501de4f37 | -4.2737 | -46.282902 | 2024-10-08 01:02:21 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b0cf381c-f40f-3763-8189-77bd087b7aac | -5.0128 | -49.5835 | 2024-10-08 01:02:21 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 138d5840-96d2-32f4-8e1c-dd76eceb1840 | -5.0146 | -49.591301 | 2024-10-08 01:02:21 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd2fe0f5-0f43-3219-bad2-40005babca35 | -5.003 | -49.5858 | 2024-10-08 01:02:22 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2626d65b-5619-3c1d-bd6b-d12e85e9c5b5 | -5.0048 | -49.593601 | 2024-10-08 01:02:22 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd8f3e05-2d4b-3495-86d7-db4c1bfc69c2 | -4.4727 | -47.7257 | 2024-10-08 01:02:23 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96d7ebc9-c55d-3032-bf37-f8a50e58e76e | -3.7072 | -45.077499 | 2024-10-08 01:02:25 | METOP-C | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 00e76258-f526-3f1e-a7ec-59aec8713f9b | -3.6975 | -45.0798 | 2024-10-08 01:02:25 | METOP-C | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a0cbcd1c-05a8-3264-938a-b60d034526df | -4.3217 | -47.6973 | 2024-10-08 01:02:25 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 902514d7-3dd7-3f86-a28c-2b1c2643d760 | -3.9377 | -46.4272 | 2024-10-08 01:02:27 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8043fb-e44e-371a-bb0d-543f8cdd3f9c | -3.9407 | -46.439499 | 2024-10-08 01:02:27 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b33b09e7-caf9-3db3-91ca-1c21b46f1d29 | -4.3606 | -48.2113 | 2024-10-08 01:02:27 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93384b5b-9022-3598-8bcb-64650d1b3f3f | -4.3628 | -48.220699 | 2024-10-08 01:02:27 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed15fe0c-153e-37ea-858b-4fab7d89aa7e | -3.9279 | -46.429501 | 2024-10-08 01:02:27 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51ee0078-fddd-34ed-b7f9-af2042721e66 | -3.9309 | -46.441799 | 2024-10-08 01:02:27 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce1cf3a-f744-3662-a6a1-a145f99dada8 | -4.3993 | -48.682098 | 2024-10-08 01:02:28 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51f5202c-6438-3efd-a6e5-73717534d619 | -4.4014 | -48.690899 | 2024-10-08 01:02:28 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f32cd81c-7e69-3b9b-87bd-8b458cda876b | -4.3896 | -48.684399 | 2024-10-08 01:02:28 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7655d331-3bf0-3583-b836-5d45c1356e62 | -4.3916 | -48.693199 | 2024-10-08 01:02:28 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcfcef36-997e-38be-8be2-17d17fdade81 | -4.8245 | -50.814499 | 2024-10-08 01:02:29 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 621b16b8-2c29-3a81-b890-a943176927dd | -4.1855 | -48.562099 | 2024-10-08 01:02:31 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17302385-b6b9-358e-8c9f-656b7699b239 | -4.0999 | -48.241901 | 2024-10-08 01:02:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6d5d0dd-905e-35e7-ad39-ebea152894c9 | -4.1021 | -48.251301 | 2024-10-08 01:02:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a333e60-d33e-31d9-a08e-21e315a6334c | -4.1043 | -48.2607 | 2024-10-08 01:02:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c3301f-1688-36b4-b71f-cdde60517d5c | -4.0923 | -48.253502 | 2024-10-08 01:02:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9630809b-49a9-3d24-bb35-b202b0fb7d40 | -4.0945 | -48.262901 | 2024-10-08 01:02:31 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b91cbfc-0288-38b7-b7ec-6d2f625ba26c | -3.9057 | -48.336201 | 2024-10-08 01:02:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a17fab14-6267-3ba1-80df-c9991c33a782 | -3.9079 | -48.345501 | 2024-10-08 01:02:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 156d01f0-62e1-340c-a3b3-04f15aff8a5f | -3.6996 | -47.5928 | 2024-10-08 01:02:35 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 234ab12c-4db1-3dc8-ae00-ebfe1c655c12 | -3.702 | -47.603199 | 2024-10-08 01:02:35 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79e1f972-393a-3e22-a12e-ef1cbf71da09 | -3.8944 | -49.519901 | 2024-10-08 01:02:39 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d10111e-5158-3e63-ac28-22b207d5351f | -3.8963 | -49.528 | 2024-10-08 01:02:39 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c83701b4-5c9a-341c-8eb9-30295e09e796 | -3.8846 | -49.522202 | 2024-10-08 01:02:39 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aac2a295-9457-33fa-a0c5-97678ea60889 | -3.8865 | -49.5303 | 2024-10-08 01:02:39 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b60e008-7dc2-3eb0-8972-047a9c0b5243 | -3.288 | -47.114601 | 2024-10-08 01:02:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9cb30f-db9f-3089-894b-700cae796a54 | -3.2907 | -47.125999 | 2024-10-08 01:02:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65e9ff5c-5a10-3551-a3c2-77b6c11b4fa2 | -4.1549 | -51.041302 | 2024-10-08 01:02:41 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c67a2889-a47f-35b3-80ad-41deda604ca2 | -4.1566 | -51.048401 | 2024-10-08 01:02:41 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7e8fdca-f417-3801-bf85-e59f7122a122 | -4.0586 | -51.115398 | 2024-10-08 01:02:43 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28a40279-178a-304c-9415-ac8137981af4 | -3.2292 | -48.923 | 2024-10-08 01:02:48 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8d9cbbe-e393-3344-bb16-c7bd99d7af44 | -3.2173 | -48.9165 | 2024-10-08 01:02:48 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad28640a-12d8-3e07-92d5-b2c57fe41bc1 | -3.2194 | -48.925301 | 2024-10-08 01:02:48 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8bd411a-e3a5-36ac-bb36-432c7ffb06a6 | -3.411 | -50.323002 | 2024-10-08 01:02:50 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b17b18ab-422e-39d8-b200-b92ec885492b | -3.6011 | -51.367401 | 2024-10-08 01:02:51 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e423e43-f915-31c9-b7e5-93a78929bd01 | -3.459 | -51.198601 | 2024-10-08 01:02:53 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac561bd5-81cf-362a-9496-6c6c8a950040 | -2.7922 | -48.552502 | 2024-10-08 01:02:53 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3062de9-4a96-3335-b941-bdc9bc78a566 | -2.7944 | -48.561901 | 2024-10-08 01:02:53 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4fb7e49-bb7e-316a-ab84-aaae7574f2b6 | -2.7966 | -48.571201 | 2024-10-08 01:02:53 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6215262a-2824-3893-852f-44734f5a9134 | -2.7846 | -48.564201 | 2024-10-08 01:02:54 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7f347d8-91d6-3b57-b28d-b805f0a41ef1 | -2.7868 | -48.573502 | 2024-10-08 01:02:54 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 604ea4a8-f3bc-34f4-93c5-09fe208daabc | -2.987 | -49.519501 | 2024-10-08 01:02:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6ce5156-9d70-3db3-a736-1c6294259e1a | -2.9889 | -49.527802 | 2024-10-08 01:02:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6d97580-26e2-3dda-a35a-95e228ce8be0 | -2.9772 | -49.521702 | 2024-10-08 01:02:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf8c1ba2-b15f-31ba-ae10-4bde0272439e | -2.9791 | -49.529999 | 2024-10-08 01:02:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16c2dd86-32ce-381c-8a66-6b3d4edf9bee | -3.1055 | -50.3843 | 2024-10-08 01:02:55 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adeb13e2-3542-3298-b034-02043f66d4f6 | -3.0341 | -50.4324 | 2024-10-08 01:02:57 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae24ec2-c2b8-3ba4-bc07-db2e8774b1bd | -3.0359 | -50.439899 | 2024-10-08 01:02:57 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e32302b-2275-3c37-a5d9-b08bf67bb557 | -2.7502 | -49.520699 | 2024-10-08 01:02:58 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de661f40-dcd4-3de3-929b-7bce14c7d310 | -2.7522 | -49.529099 | 2024-10-08 01:02:58 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6029d2c4-521f-34e3-8435-b57e759b7967 | -3.545 | -53.1432 | 2024-10-08 01:02:58 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd5d87a1-4e62-3e85-927b-3c914a97c673 | -3.0517 | -51.087399 | 2024-10-08 01:02:59 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8836369a-587f-34d7-9084-d60f3622b094 | -3.0534 | -51.094501 | 2024-10-08 01:02:59 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3afd8b10-640f-3503-84fd-79ad48fa2e90 | -2.4096 | -48.590302 | 2024-10-08 01:03:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdad3400-ff67-3d55-b2a5-3efcfdb582c6 | -2.9746 | -51.021301 | 2024-10-08 01:03:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4d123c5-c67d-35c0-a0af-52869977af6a | -2.9762 | -51.028599 | 2024-10-08 01:03:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83eae6ee-804b-3a37-b5f1-64290df947ac | -3.3309 | -53.3787 | 2024-10-08 01:03:03 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb3c9678-dacc-30c9-b0ca-da8b2a272ac9 | -3.3325 | -53.385601 | 2024-10-08 01:03:03 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50f33bc4-6771-3290-9698-b92461378533 | -3.3341 | -53.392502 | 2024-10-08 01:03:03 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2531acf1-f981-3955-963e-edb2d65f0c15 | -3.3227 | -53.387798 | 2024-10-08 01:03:03 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41d95038-f7c0-3900-a867-e6a7850b86c5 | -2.4554 | -50.2486 | 2024-10-08 01:03:05 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b27aef50-0ebe-319f-9420-9299f4b08946 | -2.4572 | -50.256401 | 2024-10-08 01:03:05 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a71eec61-7f73-30cb-9383-fc5c53d3bd4b | -3.0355 | -53.033901 | 2024-10-08 01:03:06 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff76f063-b7ea-3fad-8410-5393a3938d33 | -3.0371 | -53.040699 | 2024-10-08 01:03:06 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c91d1fc-5417-3a4a-8829-1888c162df7a | -3.379 | -54.901299 | 2024-10-08 01:03:08 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b4294d9-845c-32f0-afae-cf5ab2afa3b7 | -2.8803 | -52.8965 | 2024-10-08 01:03:08 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1373cc6c-83d8-39db-b00c-45950159ae78 | -2.8819 | -52.903301 | 2024-10-08 01:03:08 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b59d2a-5ebc-369c-ba2b-6b5a144f8b48 | -2.321 | -50.513802 | 2024-10-08 01:03:08 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)
