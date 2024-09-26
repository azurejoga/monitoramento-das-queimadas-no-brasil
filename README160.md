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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd683878-d67f-3b91-b598-acadd82d452a | -9.09429 | -61.12127 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59d6c442-8471-3474-af01-273cd57aaeca | -9.09371 | -61.12549 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43fcf412-a29d-3f28-b728-43edc3f7f764 | -9.09327 | -61.12266 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ec1b962-23e5-3bbd-8e20-6ca69ba1e816 | -9.09314 | -61.12971 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 81c0f727-e94c-3968-aaf1-c77d3792c761 | -9.09266 | -61.12687 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b95cf5eb-33f9-36a2-8e68-c5e217cde905 | -9.08993 | -61.12059 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4ab6f78-6e61-332a-8c41-69d41801f4ad | -9.08952 | -61.11777 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b382c4c-a2be-30d5-b9cb-c98a4f207334 | -9.08936 | -61.12482 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0452bc6e-7145-3b39-8430-179889bd9f0d | -9.08891 | -61.12199 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d4791a7-3a88-30bd-ba67-d1588a3f7dd7 | -9.08878 | -61.12905 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 72e08592-6640-3830-8133-c6ae3f05f694 | -9.08831 | -61.12621 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c24a7d48-8ff1-3c60-b15d-05dace26f887 | -9.08615 | -61.11572 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41faf229-c158-3bce-9b0a-e7dc1741a7f8 | -9.08557 | -61.11994 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccf43350-7a7b-35f5-8c4b-2083190a6935 | -9.08516 | -61.11714 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b346f243-a878-38a8-9f96-9dfa9379b072 | -9.085 | -61.12417 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a2fc5739-44e2-3822-beef-6d07aa6b6333 | -9.08456 | -61.12135 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f9b4ae6-235a-3d9b-a30a-cbb20553b17b | -9.08395 | -61.12557 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 788035fa-26d3-3d6f-b61e-36fbcdc44e5d | -9.01409 | -60.73154 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 244b80c5-7112-34ea-af45-4df48c442b54 | -9.01346 | -60.73596 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 519d4100-6aa8-352a-a93b-c5c09a24bd00 | -9.00899 | -60.73533 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0454cd22-2f80-3d91-b1af-22ff1e04b273 | -3.20938 | -61.07168 | 2024-09-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1766ffd2-cf02-3be9-b88d-fc40f445ac68 | -3.14237 | -60.98952 | 2024-09-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7129e080-a346-3872-9fbb-5b5c76285f83 | -3.10779 | -61.02731 | 2024-09-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58f3f3ec-0898-393f-a9e4-21954b0aeae9 | -3.09878 | -60.9506 | 2024-09-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1f121fc-4496-36d2-ac84-8c24f7516382 | -3.09825 | -60.95412 | 2024-09-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ab9be48-92da-362f-a923-17d3417bb144 | -3.07286 | -61.06849 | 2024-09-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 155d60a1-4053-3237-8297-7c79ae684aa1 | -2.98531 | -61.17553 | 2024-09-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11080f77-bbe5-3344-914d-8c2c89b8303e | -2.95986 | -61.34212 | 2024-09-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d79e256-7168-3c51-a3d5-4872f9ce1997 | -2.94147 | -60.99504 | 2024-09-26 05:46:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fb78afb-05a6-3ad7-b04e-58020b7e6420 | -3.45571 | -60.62001 | 2024-09-26 05:46:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90bf236c-2cf0-3e20-a02f-b2ee6aa9b1d6 | -3.45212 | -60.61563 | 2024-09-26 05:46:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f0ffcc4-8bc6-3b70-af24-98f65f9bda57 | -3.45156 | -60.61938 | 2024-09-26 05:46:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c68918d9-56a5-30da-8429-18e29f51ddd1 | -3.45101 | -60.62314 | 2024-09-26 05:46:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7ba14f4-af0f-3661-b80c-418c7a9157cf | -3.45045 | -60.6269 | 2024-09-26 05:46:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8db85ebd-234a-3a4c-9e7d-902e772451eb | -3.44988 | -60.61632 | 2024-09-26 05:46:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60df2885-7e99-3a72-b21d-5de111f1afca | -3.4493 | -60.62006 | 2024-09-26 05:46:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59be52b1-7319-319b-baf3-9dfeab02f19a | -3.44872 | -60.62381 | 2024-09-26 05:46:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aef6311f-895e-39f4-95c7-a971f062dbab | -3.09363 | -60.46395 | 2024-09-26 05:46:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e9c5f08-3994-36f9-93f3-b8324e290ec8 | -3.08946 | -60.46333 | 2024-09-26 05:46:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1de09cb0-dcc1-3011-bcbb-53d4453e1d95 | -3.6827 | -60.48212 | 2024-09-26 05:46:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd7b56d4-066f-3847-acf1-8a921b459aee | -7.2978 | -61.09454 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c6abf351-42e1-33bf-8439-8f6b287d7f53 | -7.29723 | -61.09853 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3e8dada5-da46-3b5f-9c84-80ed162ea97a | -7.29355 | -61.0939 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ce0c2645-f94e-32dc-94ef-991b8b1915a4 | -7.29298 | -61.09789 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 58c4caf5-8c94-3635-b513-8a515ea86341 | -7.29241 | -61.10188 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3bb445f1-b5df-3d94-b7d3-c002a3b814d5 | -7.28929 | -61.09328 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43a23122-197b-3b7e-a545-7097a02ead49 | -7.28873 | -61.09726 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8bae9a1-0533-35df-954d-c0b064d8c621 | -7.28817 | -61.10122 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 781f450e-61d6-303d-ba24-d2a830d94bb8 | -7.28335 | -61.10461 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0773555d-9ff6-3293-9355-8354dd7e6bf4 | -7.28278 | -61.10862 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db6b920c-f991-3c52-a03a-46e2c9593376 | -7.26249 | -61.10217 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac574476-6b64-35d0-a4c1-933e18b8f278 | -7.26208 | -61.10157 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcddc254-150f-316f-a96c-b604648452bd | -7.26153 | -61.10555 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03b65b2c-93ed-396f-bf26-d7be8fbc047e | -7.25824 | -61.10153 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8e5579a-a2ac-3217-b573-1f5b641d35af | -7.25784 | -61.10093 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb575fe0-8638-359f-80b7-84d538d164f9 | -7.25766 | -61.10549 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a056f20b-d93e-338b-9761-45304e99b644 | -7.25728 | -61.10489 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a77f2b9-9abf-3a2f-ad8b-ac90594b2297 | -7.25399 | -61.1009 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c613cff-4043-3e17-804a-cf8d6250fa70 | -7.24974 | -61.10028 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8b8881c-5133-34a5-a1bd-32ff62bdbfde | -7.90674 | -61.51221 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6381b72c-bbc1-36d3-b1c0-65ac9b6e06ff | -7.86596 | -61.76638 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e294e3f-5d71-395d-bafe-51fcd77325d6 | -7.84839 | -61.34615 | 2024-09-26 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8978902e-c9b8-34fd-9af6-b694a4cc3400 | -7.73697 | -61.10013 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89dd8d07-1583-36c3-b67e-e3f69644643f | -7.73639 | -61.10418 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be2b670a-94e2-3e58-ad49-a71938deae7a | -7.73153 | -61.10768 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 620a32e4-4a79-367f-aa43-134b74d365e3 | -7.72725 | -61.10707 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be90dcae-8fd3-3e04-b14d-da1c40193f8e | -7.72668 | -61.1111 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ada18009-37ce-3412-8c30-18d0f9ed42f6 | -7.00549 | -60.68162 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fb9870e-aa2f-3ede-b770-b87b9c8bdfac | -7.00541 | -60.68861 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67334358-8e8b-3ffd-8305-e43ab1a39736 | -7.00425 | -60.68999 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 906791fc-0349-34b8-96d1-e40b42a0d1a0 | -7.00165 | -60.68378 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea323359-3746-382e-828e-4f8d60f56f3f | -9.13183 | -61.35931 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d53e1d32-8aa8-3bc9-98b1-d693583faf57 | -9.13126 | -61.3634 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed4498cb-1cb4-3fe1-a346-2ac0600c5881 | -9.13068 | -61.36746 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc345478-11e7-3be6-a3db-ff983821cf52 | -9.1287 | -61.35051 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43835f6f-85bc-3e68-bf63-a985c85d6c50 | -9.12812 | -61.35462 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc90004e-d9a5-3bc7-be28-9f1bf666b65b | -9.12754 | -61.3587 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d87e230c-d5c6-3e1e-8af5-14868172ea3f | -9.12696 | -61.36278 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca5d1021-43bc-342e-8546-b96e05a5f5b7 | -9.12556 | -61.34169 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad0bee05-f04d-303a-a9c8-31f93f631025 | -9.12498 | -61.34578 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3d05736-3d52-311a-a410-148ffa333a65 | -9.1244 | -61.34989 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d45dc63d-30ac-33ef-8da4-d93f2bbfbfd1 | -9.12383 | -61.35399 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a50f60cb-4afb-3269-8968-38f1d2a9b528 | -9.12325 | -61.35808 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce4d099b-991a-3658-b75e-d58545c1d466 | -9.12241 | -61.33294 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a2d7384f-3e9d-3305-a669-6dd6e9166655 | -9.12184 | -61.33701 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 74c3856a-f06c-36eb-a144-f05ddedae9dc | -9.12126 | -61.34108 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0bf6d735-da32-3f8f-aa8d-ce9b37f95b1e | -9.12098 | -61.31186 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e6b4e8a-0992-3cda-96cf-f13b59eadbc0 | -9.12069 | -61.34517 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79f554cb-e9bb-38c9-96c2-4d849d27d594 | -9.1204 | -61.31597 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e19246bb-172a-37ca-aef4-c11d825bf357 | -9.12011 | -61.34926 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f3da813-b5ce-3998-aefb-8725471ba39d | -9.11983 | -61.32007 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15d1a868-79ba-3639-a39c-6051b9e4953d | -9.11953 | -61.35336 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbfe39a8-8aa6-352d-b409-5bf00dcf6af3 | -9.11925 | -61.32418 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 06e7082f-8516-39f1-9272-7b63af7b9516 | -9.11896 | -61.35747 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b45c1e1b-a7c0-3fb5-b9eb-d44d0bffd437 | -9.11868 | -61.32829 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b12ddd57-255f-3ad6-88ec-0e47bf3b210d | -9.1181 | -61.33237 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 80763e43-ba4c-318c-afcd-82cec79b5e9a | -9.11753 | -61.33644 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d7e489e-fe6a-3d39-bd0a-21ea835805f4 | -9.11696 | -61.3405 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fe20dbec-5b7e-3b70-853a-3dd2b0ac6995 | -9.11639 | -61.34454 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87f7d285-4231-30e2-9012-a15ed02ba0c1 | -9.11582 | -61.34863 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README161.md)
