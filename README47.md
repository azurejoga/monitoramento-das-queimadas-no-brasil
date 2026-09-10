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
| a5c8090b-6284-3942-9b06-c151a587ed4e | -7.4976 | -45.2814 | 2026-09-10 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 75b7f8e7-eacd-3d03-9bb1-ab4c792e0e2d | -10.6621 | -45.9974 | 2026-09-10 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 325610a7-db28-332e-869e-0f6b1acfee78 | -12.8552 | -44.3389 | 2026-09-10 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e7f0694f-17ba-3808-8c95-93c4df50a897 | -14.61652 | -48.86251 | 2026-09-10 12:10:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4a2bb68a-0e1b-384b-bf1a-6dba3bfd465e | -14.94069 | -47.02641 | 2026-09-10 12:10:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 2ac9ede1-af1a-315d-81bd-6704acecad0b | -14.93285 | -47.04358 | 2026-09-10 12:10:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 3f5d2b43-2d87-3006-a73c-b3ef9c452176 | -14.9381 | -47.0509 | 2026-09-10 12:10:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| eb2644bf-92bb-3af0-91dd-c7e41eca0266 | -16.75978 | -47.12307 | 2026-09-10 12:10:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fcb219d0-ac1b-332d-b7b9-30f7eea47f2d | -18.03812 | -51.22356 | 2026-09-10 12:12:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ea0d2ab2-2c39-3292-9ac6-5a33fd517210 | -18.47756 | -51.72004 | 2026-09-10 12:12:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b76c631a-a5f2-39cb-8327-0c6e71a135e3 | -18.47914 | -51.70737 | 2026-09-10 12:12:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5cdb8227-ee02-31c4-80bf-88742c73377e | -7.4979 | -45.2587 | 2026-09-10 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 4719fb70-9698-3023-983e-2ee53210a169 | -7.587 | -45.6804 | 2026-09-10 12:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f60265ed-3890-3690-883e-929e67e35be0 | -12.8552 | -44.3389 | 2026-09-10 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 7c9c118e-927f-332e-b0e8-62516140ce89 | -12.8359 | -44.3422 | 2026-09-10 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 5cbb7a61-334f-326a-b27f-c138488220a9 | -7.4976 | -45.2814 | 2026-09-10 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 54abb999-be28-3577-afc8-09fa5e853f15 | -6.1726 | -44.6432 | 2026-09-10 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 8a02acc7-d4bb-33dc-afa5-403589e2afcd | -10.7395 | -45.9194 | 2026-09-10 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| c19869db-1870-323f-87bc-f7b323b86fc5 | -7.9834 | -43.9951 | 2026-09-10 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f6096ba7-17d1-3bb3-bb27-4885e595472f | -7.4976 | -45.2814 | 2026-09-10 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 50527044-f04a-3026-9604-0852c519a1a5 | -10.6985 | -46.106 | 2026-09-10 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 69f912d9-72ec-3377-8ed3-9d024263cd98 | -10.6981 | -46.1287 | 2026-09-10 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| c326530b-5471-3a0f-9191-b715eea2e4aa | -12.8359 | -44.3422 | 2026-09-10 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 7a91fcc1-3a42-389c-9598-bf762738c4ee | -12.8552 | -44.3389 | 2026-09-10 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 96cf8b67-4c97-3b46-a947-5f2d2baf4fc1 | -10.7395 | -45.9194 | 2026-09-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 2275b9b4-accc-3e8f-9b2a-8c4eea17c1e9 | -7.4976 | -45.2814 | 2026-09-10 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 446c8f34-147b-3210-bcee-cea550d497da | -7.587 | -45.6804 | 2026-09-10 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 93f24328-185e-3499-90b4-fd539495a300 | -12.8359 | -44.3422 | 2026-09-10 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 48dde257-7982-3bb5-9aaf-d0e02ffd1b10 | -10.7398 | -45.8967 | 2026-09-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 81e582fe-7bba-32dc-b3af-a70b2e6a2852 | -10.6981 | -46.1287 | 2026-09-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| d7c80665-c7d9-3d76-a9db-983fe169676e | -6.1726 | -44.6432 | 2026-09-10 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 529d1f86-0b6c-31d0-9001-3c57f76bc759 | -12.8552 | -44.3389 | 2026-09-10 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| e9465dd7-d5c9-3d09-81de-f447369dd21c | -9.7892 | -43.4564 | 2026-09-10 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a83e155f-bf59-3c34-953d-155a714ab9c1 | -10.6985 | -46.106 | 2026-09-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 29a659f7-767d-3eb9-ad92-3752fdbe0591 | -5.7756 | -45.0826 | 2026-09-10 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 42458542-4499-3dda-b89c-d00638a33bf9 | -12.8359 | -44.3422 | 2026-09-10 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 6bf3aaa6-6671-3812-b56e-024dd387f503 | -10.6981 | -46.1287 | 2026-09-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 219.9 |
| e518aebc-68f3-30c9-a657-6d6c0ce13de0 | -10.2365 | -45.2546 | 2026-09-10 12:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 4e477ea4-80be-30bc-8cd2-374a2b5d794f | -12.8552 | -44.3389 | 2026-09-10 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 8146ecbb-db49-3f72-abc4-ec86c139c55d | -10.7585 | -45.917 | 2026-09-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6fd78700-f52f-32d8-812a-90fbb0dbb3c5 | -7.5167 | -45.2569 | 2026-09-10 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3b9eb1bc-50fd-329d-b0a5-c499c05f34ce | -10.6985 | -46.106 | 2026-09-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 6f859c87-07e6-34f4-b368-c1553cab0b95 | -10.2175 | -45.257 | 2026-09-10 12:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 0d835595-d898-388c-b3de-f06f0a67e85e | -7.4976 | -45.2814 | 2026-09-10 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 24a1c900-ed64-3f2c-bcee-aeaacbbfbb01 | -7.9834 | -43.9951 | 2026-09-10 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2436eb95-288e-34c8-93f5-b002a02c1755 | -7.587 | -45.6804 | 2026-09-10 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b87010cb-ab82-3c2d-9eb5-37e4d8a5d303 | -10.7582 | -45.9397 | 2026-09-10 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| a75ac578-9883-34b9-9bd0-ccec7760e91f | -7.4788 | -45.2831 | 2026-09-10 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 7dfd181f-f680-3f94-90b7-2ffef4bd0e3c | -6.1726 | -44.6432 | 2026-09-10 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 2e4d5f5f-144a-35dd-b841-53b0f0e256db | -10.6981 | -46.1287 | 2026-09-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| b97b9946-786d-3802-82eb-549ffde1cd35 | -10.7585 | -45.917 | 2026-09-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| cd6d1aee-8a5c-384c-9838-5387cee5d572 | -10.7398 | -45.8967 | 2026-09-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| e2121d97-5415-3084-ba6e-8bd953b4f52a | -10.7582 | -45.9397 | 2026-09-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| d7e5c16c-6a78-3ef9-b4f1-06fb137dfa32 | -6.9155 | -45.3104 | 2026-09-10 13:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 3ed91bee-54aa-3906-a458-0984bf093c9e | -9.7889 | -43.48 | 2026-09-10 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 60e39b19-2bbe-3fe2-a42e-4db5fe942635 | -7.4976 | -45.2814 | 2026-09-10 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| d8117b28-5a88-3ad2-b5e9-96faf74189a2 | -7.587 | -45.6804 | 2026-09-10 13:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fe335dd0-df93-324e-a1d8-c3c1781ac41d | -9.7885 | -43.5036 | 2026-09-10 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| b4212c42-5b3f-3976-836d-5e05f339b531 | -6.1538 | -44.6446 | 2026-09-10 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 80c7cc58-cf90-3c4c-a48c-bc6fdc8b43c5 | -10.7395 | -45.9194 | 2026-09-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 253.9 |
| 386932e2-6aeb-3114-a586-98ae375f2d6c | -9.793 | -47.0672 | 2026-09-10 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| de2c299c-8112-3edf-958e-0a61d9d3e132 | -7.9834 | -43.9951 | 2026-09-10 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 8e000875-0628-304f-bef8-05280b3b6c59 | -11.3326 | -45.772 | 2026-09-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.2 |
| 0ea6ca9e-8ff7-3410-a1f3-6bbe53b001c6 | -10.6985 | -46.106 | 2026-09-10 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 372c0d79-bce2-3344-b83b-cfeb00c25d28 | -8.744 | -62.379 | 2026-09-10 13:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 310fb141-616a-3e3d-9650-b6df353030c1 | -9.7933 | -47.0449 | 2026-09-10 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 7edd7379-5ddd-3c1e-9235-8e8c9aa0e992 | -9.7889 | -43.48 | 2026-09-10 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| bf84f4d1-d34c-308c-a5fc-7c18e9d5550a | -9.7885 | -43.5036 | 2026-09-10 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| f149fc0b-c70d-3d39-90fe-1c8a91d91e6f | -6.7077 | -45.4635 | 2026-09-10 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 99426f6d-4e68-3658-8f9f-c9827e23fcf6 | -7.587 | -45.6804 | 2026-09-10 13:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 247.9 |
| 2fcd5b2b-45c1-36f4-bc5a-341b402aacd0 | -10.6981 | -46.1287 | 2026-09-10 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 800f11ce-2383-32a0-90b4-3f68e838721d | -7.9834 | -43.9951 | 2026-09-10 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c8f0073b-2906-3de7-a81f-9a6f4fa23a71 | -7.5682 | -45.6821 | 2026-09-10 13:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e2c3331b-a7c3-3767-a575-77818d06f878 | -9.793 | -47.0672 | 2026-09-10 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 16d56d8d-688f-320d-a24d-a19fa667ecae | -2.7331 | -57.6271 | 2026-09-10 13:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 0ceba9bf-399b-3c91-9014-3c6cbfe52cdc | -9.7933 | -47.0449 | 2026-09-10 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| e1fce3a0-6597-32c9-93c9-0b69273d2201 | -6.1726 | -44.6432 | 2026-09-10 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7a697dab-18cf-3ca8-90d1-e09def3cd5ad | -7.4976 | -45.2814 | 2026-09-10 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 17bfee63-ae08-3b01-a1fb-cf10a4d333f1 | -6.7863 | -58.8995 | 2026-09-10 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a14adf3f-2b2b-31db-aba0-c4b4fd77ee97 | -10.5501 | -47.1126 | 2026-09-10 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| bbd6bd48-14fd-3e87-9892-16ee4a1e5708 | -9.7141 | -43.3956 | 2026-09-10 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 02248588-bcad-3505-b3f6-aaa485628228 | -10.7585 | -45.917 | 2026-09-10 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 4de68ddb-84d6-3401-bde6-7b6f5e39c712 | -9.793 | -47.0672 | 2026-09-10 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| ea2cf339-8917-3d4c-81ba-e5f6b23ff0c6 | -7.9834 | -43.9951 | 2026-09-10 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 6edd038f-5c1d-3ed0-a53a-6df1029a9f9d | -9.7885 | -43.5036 | 2026-09-10 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 27827c6c-f379-3991-b118-de8f19b06314 | -6.7077 | -45.4635 | 2026-09-10 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |
| ade13b9e-1624-36aa-b2b9-f60183cd8157 | -2.7331 | -57.6271 | 2026-09-10 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 893b6b07-97f6-3f8c-98c3-b23d7fdbc18a | -7.4976 | -45.2814 | 2026-09-10 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a64b520e-125b-3e4b-9d29-c83ca17d1c59 | -9.7141 | -43.3956 | 2026-09-10 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 7a57e6c8-c17c-30e4-91a5-a25a15bf03ff | -10.7582 | -45.9397 | 2026-09-10 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 371.4 |
| fad50638-cc4a-3f42-8ec1-e2ee7a408e73 | -6.1726 | -44.6432 | 2026-09-10 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c2d657c8-8288-3045-911b-a4c4c0cb32ee | -3.4058 | -59.2347 | 2026-09-10 13:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 7cb6616e-0c5d-3801-9a15-e5a646031760 | -9.7889 | -43.48 | 2026-09-10 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| f9ed0b8f-8761-3ae2-8d6f-5b43cd946432 | -10.7578 | -45.9624 | 2026-09-10 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 6d9e240b-a909-3d3a-b6eb-2068b2a40ceb | -9.7933 | -47.0449 | 2026-09-10 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 78e09a23-aa4c-3261-b92e-b6f104de914b | -6.7863 | -58.8995 | 2026-09-10 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0120a561-dcd2-3a50-89e5-959a99d565e8 | -10.0697 | -46.2516 | 2026-09-10 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0204c750-9839-3045-aac0-878989f6c4b3 | -8.8982 | -61.4393 | 2026-09-10 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 79d5197b-23cf-3172-bc3f-74c0c6382da1 | -10.6985 | -46.106 | 2026-09-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 84317c27-9d43-3cd8-b1d1-75dd5eb274fd | -7.9834 | -43.9951 | 2026-09-10 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 165.3 |


[Clique aqui para ver as próximas entradas](README48.md)
