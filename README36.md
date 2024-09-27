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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc360ec5-5201-3985-b3dd-181d53b09b31 | -8.1313 | -61.3381 | 2024-09-27 01:29:38 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7fe6ba-d390-3568-a876-0d132f1381fb | -8.133 | -61.346001 | 2024-09-27 01:29:38 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68c98407-b6da-3a4b-bec8-0b165ac74596 | -8.1215 | -61.340199 | 2024-09-27 01:29:38 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72539acb-725e-3965-b67d-a27ed04c8038 | -8.1232 | -61.348099 | 2024-09-27 01:29:38 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1e75f59-29e2-36d3-b7e8-ad966a004274 | -8.086 | -61.273102 | 2024-09-27 01:29:39 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d24a3908-2b60-3a93-8624-bc963376aa6f | -8.0878 | -61.280998 | 2024-09-27 01:29:39 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73b36990-f387-37a5-a674-b9518e78febc | -8.5024 | -63.505299 | 2024-09-27 01:29:40 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7b41012a-26a3-345a-90fc-ceaa8e5b7b11 | -7.992 | -61.219398 | 2024-09-27 01:29:40 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3db54a63-3805-3a7f-a6d6-a556f3793ca7 | -7.9206 | -61.268101 | 2024-09-27 01:29:41 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ca3cc32-5601-35e2-9f28-4602899b9e45 | -7.9223 | -61.275902 | 2024-09-27 01:29:41 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42183ebf-d69f-3f62-bc7c-26898ed2f09a | -7.9241 | -61.283798 | 2024-09-27 01:29:41 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 744fe516-2113-38eb-9587-1d88a48c5460 | -7.9108 | -61.270199 | 2024-09-27 01:29:41 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4074af68-e0ea-363a-8366-154839492845 | -7.9125 | -61.278 | 2024-09-27 01:29:41 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d312a15-db0d-3201-83a3-5b60f9584d02 | -7.7786 | -61.184299 | 2024-09-27 01:29:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9355571-7811-3029-b144-ca2b4c3384ea | -7.7803 | -61.192101 | 2024-09-27 01:29:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1f70714-85a7-30c5-b577-f7e472abddc6 | -7.7671 | -61.178699 | 2024-09-27 01:29:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09501d6f-2f92-399b-9d84-0d999805105f | -7.7688 | -61.186501 | 2024-09-27 01:29:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca20d5c1-eea9-38c1-a375-2aeba644258f | -7.7705 | -61.194302 | 2024-09-27 01:29:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2530523-f85b-3492-a579-46f6a6ab412f | -7.7723 | -61.202099 | 2024-09-27 01:29:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9fed9bc-e932-37b3-8eec-ca51d1cfa77e | -7.7446 | -61.216202 | 2024-09-27 01:29:44 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c7cc12d-dbec-3cf5-abbd-1498f0f0c887 | -7.7463 | -61.224098 | 2024-09-27 01:29:44 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98c9ab23-cd3d-3b2b-8167-16b6b28af040 | -4.5714 | -47.995098 | 2024-09-27 01:29:44 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9ea0317-9e69-34f8-8edb-8de4eb8aaca7 | -4.5618 | -47.997501 | 2024-09-27 01:29:45 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79129f6f-2277-3eda-8b48-c41360d0c138 | -8.9934 | -67.337502 | 2024-09-27 01:29:45 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a6b7877-7cb8-396a-a126-edaf3f568fee | -8.9973 | -67.357002 | 2024-09-27 01:29:45 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f148f9b-f914-325d-a689-2548e0276e65 | -9.0014 | -67.376503 | 2024-09-27 01:29:45 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cdca117-d89d-3143-9a55-a3540bc10b25 | -8.9876 | -67.359001 | 2024-09-27 01:29:45 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81558059-420b-31f8-93a5-e8fdbd8df3c3 | -8.9917 | -67.378502 | 2024-09-27 01:29:45 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69aa0f44-95b5-309f-a756-439e9e6cdd61 | -7.3951 | -60.297199 | 2024-09-27 01:29:46 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61587ab9-0269-3e1c-a632-83e2ad2ab841 | -8.2049 | -64.070702 | 2024-09-27 01:29:47 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8400a64-e5fe-321d-98b5-14259c24ce3d | -8.2073 | -64.0821 | 2024-09-27 01:29:47 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7727db3-661c-3ec3-87b4-19af50b36116 | -7.5321 | -61.369701 | 2024-09-27 01:29:48 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 371fd458-5378-39ae-9573-ab74d1bc264d | -7.5338 | -61.377602 | 2024-09-27 01:29:48 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5cbc9f97-c534-3624-9d6b-8b05e2bc2926 | -7.5356 | -61.385502 | 2024-09-27 01:29:48 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2a76b3-19e6-321f-aabc-1530aa3a40dd | -7.5223 | -61.371899 | 2024-09-27 01:29:48 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2028c6a-f7fe-359e-a343-399e03ca71cc | -7.524 | -61.379799 | 2024-09-27 01:29:48 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f4dabc8-0881-36b0-9369-7d84920e08bf | -7.5258 | -61.3876 | 2024-09-27 01:29:48 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f671767-0618-30cc-bad7-6a303b7c0d74 | -7.5194 | -61.497101 | 2024-09-27 01:29:49 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b222916f-53ff-3a43-9daf-fbef746d62f9 | -7.5211 | -61.5051 | 2024-09-27 01:29:49 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5279691a-f7ed-344b-a2e1-fff853841aa0 | -6.9595 | -59.2374 | 2024-09-27 01:29:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac87f060-b23c-3345-ae64-7d80a65b9524 | -6.9611 | -59.244301 | 2024-09-27 01:29:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f97b534-1f40-3180-b614-ded5f08cf2f2 | -7.2221 | -60.6721 | 2024-09-27 01:29:50 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89073bac-9d01-3424-a079-fd422f60a97b | -7.209 | -60.6595 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7bc5f9d-5da2-3d09-a92a-8c7d87681f48 | -7.2106 | -60.666901 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1e1faad-8921-38b6-af23-97ee0be2437b | -7.2123 | -60.674301 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba74aa7e-7160-3228-96b2-3fe8a1a38744 | -7.2139 | -60.681599 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a04358d8-a038-39ab-8bc3-08c2fa3472de | -7.3028 | -61.078899 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ebef28f-060e-34f9-8b56-d712fce184ac | -7.3045 | -61.086498 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0d059d1-909e-33af-ba4c-06b2ffcd238f | -7.3062 | -61.0942 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff664b5-94e5-38b7-b054-4ed4752b6514 | -7.3233 | -61.170799 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 120d227a-61ae-3ee1-a843-ebbb57344a08 | -7.325 | -61.178501 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75200f56-037e-31f4-846c-d7881c705f26 | -7.1975 | -60.654301 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cda6277-a6fe-3a7a-9181-0d0201bbace6 | -7.1991 | -60.661701 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4e24921-0345-33ce-a9a7-2f7b057d1d5b | -7.2008 | -60.669102 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46f2689c-32d7-3f40-8cf5-534b663d7100 | -7.2024 | -60.676399 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f456477e-5dec-34e4-9916-8a4dacac674a | -7.2041 | -60.6838 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06567ef6-a1c0-34e3-9025-b8175e817eba | -7.293 | -61.081001 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6026aa1-0625-3401-b672-606ce915dead | -7.2947 | -61.0886 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 844f0708-0675-3f74-9815-e7941e3999d7 | -7.2964 | -61.096298 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4954b4b1-45e9-3a44-a118-37c787936064 | -7.2981 | -61.103901 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b190b90-c27b-3d98-9f70-c1dab3283a16 | -7.3152 | -61.180599 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3ba1082-b81b-3d35-b568-5522cbbef853 | -7.1926 | -60.6786 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 017aa332-b7ac-3d05-ac19-f7ece2b87d5b | -7.1943 | -60.686001 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6bf16aa-17f0-3ad4-a752-1ad61be26564 | -7.2849 | -61.090801 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b384f2cb-5c0d-3270-a6b9-8fd054f1cc7e | -7.2866 | -61.098499 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fc07b1d6-63d3-396e-96e2-1b1e8a23cd5d | -7.2768 | -61.100601 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0376f23-5393-3fce-bb78-0684fe7d6949 | -7.2785 | -61.1082 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0923e03e-af23-3c23-9447-d7ca776213ec | -7.2555 | -61.097301 | 2024-09-27 01:29:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72d9686f-8e16-3e8e-b024-990bc8a1d489 | -6.8974 | -59.643799 | 2024-09-27 01:29:52 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83070239-783e-388a-8378-7e3ab3fbf70e | -6.8989 | -59.6507 | 2024-09-27 01:29:52 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c33f4319-f2e2-3885-802a-877e9994e9bc | -6.7807 | -59.3573 | 2024-09-27 01:29:53 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 004abf4b-32b7-36b2-957b-afbf8343ed0b | -6.7905 | -59.355099 | 2024-09-27 01:29:53 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 782b718a-6fe5-3f41-a2a7-4d94317c15fb | -6.7921 | -59.3619 | 2024-09-27 01:29:53 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e79848d3-7730-3db6-bd08-a104d3b82796 | -6.7823 | -59.364101 | 2024-09-27 01:29:53 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2380679f-6f01-3330-9805-50189d7669be | -4.1943 | -48.610001 | 2024-09-27 01:29:53 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dcfcb82-af28-36bc-8014-bd0a76fd3193 | -4.2008 | -48.636101 | 2024-09-27 01:29:53 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e215fec-76d7-357d-ac51-d4eec043841d | -7.0063 | -60.6735 | 2024-09-27 01:29:54 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84758a49-a225-3b3b-a2b9-afdf44ae2c7c | -7.008 | -60.680801 | 2024-09-27 01:29:54 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f37ed8bb-bca2-336d-afed-a0d33da39d19 | -7.4737 | -63.434101 | 2024-09-27 01:29:56 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd032fb-263e-3c98-b758-b8be80f2dcce | -7.4759 | -63.444199 | 2024-09-27 01:29:56 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59f1719a-59d9-3aea-8d1f-9b9065c21582 | -7.464 | -63.436199 | 2024-09-27 01:29:56 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89f3fa8c-df45-3c27-a8db-bbe63a36cf15 | -6.6374 | -59.951099 | 2024-09-27 01:29:57 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0c5bddc-21a3-36e2-b3b2-95528b14a400 | -6.639 | -59.958099 | 2024-09-27 01:29:57 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8879a86-10d5-366e-89bf-fcf11af79716 | -6.6146 | -59.941399 | 2024-09-27 01:29:58 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19b81b8b-7865-3474-b635-30c7d460669f | -6.6045 | -59.9879 | 2024-09-27 01:29:58 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c3bb6c2-1844-3cbc-a4ad-e37e6a799f26 | -6.6061 | -59.9949 | 2024-09-27 01:29:58 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67226e89-b90a-303a-8f12-3f36d24ecd98 | -6.6077 | -60.0019 | 2024-09-27 01:29:58 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24732903-8e6d-37b3-a0cc-eb80f6a1cf23 | -6.5765 | -60.045799 | 2024-09-27 01:29:59 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4b15c3b-69d2-3674-8e29-36843ee58ab8 | -6.5667 | -60.048 | 2024-09-27 01:29:59 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe2306aa-fa4e-3bd5-a5e1-a84772f4d11c | -6.5683 | -60.055 | 2024-09-27 01:29:59 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3526f7e8-599c-3932-a944-84b5f3f04545 | -6.5699 | -60.062 | 2024-09-27 01:29:59 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64966f94-c65a-3c95-8106-c97a71103d20 | -6.3876 | -59.984798 | 2024-09-27 01:30:01 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2352be0c-f3f2-3d93-bae8-af50f5d356fa | -3.5736 | -50.5788 | 2024-09-27 01:30:11 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e04a3f76-32bb-3e2a-b905-ba011657701a | -4.5067 | -54.943199 | 2024-09-27 01:30:13 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24345478-0ad6-334b-8582-dc55ead00c44 | -4.509 | -54.9529 | 2024-09-27 01:30:13 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e7e810b-ef71-3a06-832e-c84af70c2d9e | -4.4849 | -54.938 | 2024-09-27 01:30:13 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95b28abe-5b1d-3d62-8040-36f00d884925 | -4.4872 | -54.947701 | 2024-09-27 01:30:13 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d8576b5-1f5e-3690-b608-95689da234f0 | -4.4866 | -54.988701 | 2024-09-27 01:30:13 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f59935-eb0d-3264-9fd5-5c10789765c5 | -3.1989 | -51.146599 | 2024-09-27 01:30:19 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa1014f0-a05f-374d-b41e-3f0b16f4f5a2 | -3.2033 | -51.1647 | 2024-09-27 01:30:19 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README37.md)
