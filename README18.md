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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 889574a6-d360-3ce9-aa7b-e3295bb82b8f | -5.34769 | -56.02119 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f028980b-19a4-3d2b-99b5-9f1182a30ba3 | -9.31424 | -47.63325 | 2026-09-06 04:46:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65cb2c3c-2070-35df-9fff-27807c96f31e | -6.13401 | -57.69146 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ea05099-588f-340d-ba03-ba578d468908 | -5.13474 | -56.27277 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| b49845df-1569-3621-affc-97d008480dc0 | -7.36948 | -47.01619 | 2026-09-06 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0b38969-eb3e-3a65-a8f9-11ddf3649bbd | -4.3695 | -47.77683 | 2026-09-06 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee096c8e-64ea-3583-b5ea-6ea315488bbd | -6.87775 | -55.60651 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 42d0cfee-bfec-38d8-9809-bb3ee540ca50 | -6.05509 | -57.79065 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d61578a-b307-31f0-aad0-5b79cdd4978a | -7.1093 | -56.51243 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6aaa1179-b91d-3de2-be83-b9b4c3956268 | -5.36093 | -56.01618 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 604dcabf-f3f9-36e1-8d9c-c70f01166331 | -3.54246 | -48.18481 | 2026-09-06 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d8a5aca-7d46-34c5-902a-324a71de137e | -8.98196 | -44.41079 | 2026-09-06 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9242e100-d3e2-3fdd-8d97-aadca6ce5cce | -6.87391 | -55.60587 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6cdafff6-d0af-3646-8feb-e0345223079b | -5.85199 | -52.05105 | 2026-09-06 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54a9379d-43aa-33de-93dd-92aa46cf205f | -11.33247 | -45.07035 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| bcecf210-0c27-3888-aa59-62ed57db5c67 | -5.17189 | -56.0511 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5fdfc1e-1de8-3fb6-a90e-26488e3ef32b | -8.50322 | -54.65607 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2302347-c76b-3e3b-a30b-9eea7cfd9397 | -5.36094 | -56.04166 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bbf72ed-b969-3c4c-9964-a39711e6a0cd | -7.09714 | -56.51038 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7629175-3277-316f-823d-927035988572 | -7.10463 | -56.51543 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b136f6a6-c5c3-3b85-afae-245e7914f021 | -6.8808 | -55.61188 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4218b08-4339-3696-a29d-b816dc5cd6d7 | -5.85006 | -60.25709 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05176986-f0d8-3734-905a-fa7bb42e8b87 | -4.67156 | -55.62909 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9e8f7f9b-ca6d-3661-88ff-36fa32da3683 | -5.33787 | -56.03053 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8ba0d16-8335-3f7e-ae27-0cdbaeea58c7 | -5.36902 | -56.043 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 92df52ab-ddd5-3130-a775-340b215c5d66 | -4.22866 | -48.37099 | 2026-09-06 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a5ac418-01b1-3b15-9296-bd3076c8ed85 | -4.97545 | -56.00023 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7982b523-8cff-3e31-8c0e-ff1c1469a52b | -3.23293 | -58.89071 | 2026-09-06 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e6d6e08-7012-3a1b-a736-084aa21e8246 | -3.80438 | -55.88066 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce219ef8-8f1e-3bd1-8035-0609fc8e8fbc | -5.1525 | -55.96227 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 60157dfb-4879-3916-8fd8-64c1830ba0c9 | -4.89949 | -45.09816 | 2026-09-06 04:46:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c2f2fc5-f681-38a5-b1e9-dc8b85696118 | -5.14846 | -55.96163 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 61f29322-f94c-3240-87b5-f22d12f464fe | -5.89499 | -44.73512 | 2026-09-06 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bed42b8-af2e-3f6e-bcfa-e16f2a30bb53 | -6.44202 | -58.15558 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af353052-8f23-3a87-91a7-f3d127f73c38 | -5.41369 | -45.24839 | 2026-09-06 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f2fde36-cc18-3075-a948-7ed35b5a404d | -2.45538 | -57.91131 | 2026-09-06 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aaa0e943-a098-358f-a905-dc5f45c2c215 | -4.11616 | -49.08655 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7736ae6a-28e6-3ae0-aa0f-80e870495a36 | -5.65326 | -60.24142 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7801248f-7586-34af-82d0-691be3855cda | -6.11653 | -55.82198 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aec3bdbf-a260-3cfa-ae6f-8c42e2e42d39 | -5.35633 | -56.01903 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 42b69256-e22c-33c4-80a7-96e99ca284b9 | -9.63565 | -47.6826 | 2026-09-06 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eedc56a9-d324-377b-974f-6098707735e3 | -8.96859 | -44.40327 | 2026-09-06 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ef6f49d-2cd8-3df9-a6d1-d701a92cd724 | -3.38375 | -59.41333 | 2026-09-06 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e4e5b42-d533-3c1f-b04d-41ad21faf4d3 | -5.33383 | -56.02988 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d49174a2-0619-3937-b8c7-07ee99d185d6 | -4.67044 | -55.63609 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b684a19-8a82-3ee7-b432-ac8cc52784b6 | -5.35633 | -56.04454 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0b091d6-721c-37ef-9395-a22cc796636f | -11.29436 | -45.10859 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3a471789-d475-353b-9adf-b16b474cda89 | -4.92357 | -55.80622 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c27dc7a-9480-361c-9cdd-b27b6bf2ba2d | -3.238 | -58.89152 | 2026-09-06 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e1ff270-ee9a-3f0a-a41a-793ef168e769 | -4.47405 | -55.08648 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5efad07-9fa1-31f5-afda-15c3db64057a | -3.86123 | -51.03792 | 2026-09-06 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 626e12fb-e38a-38c5-9497-958d0507f92a | -5.14385 | -55.96454 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 04e15ce6-a9f5-3312-b3cf-16bc8a47354a | -3.81198 | -55.88559 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 452ba50a-85ed-3ad2-ac23-9e25ec440f92 | -5.3696 | -56.03944 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4e4a035f-680a-345d-9ca1-992ecee0e714 | -3.89874 | -57.16842 | 2026-09-06 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d814339d-1402-35a2-aefc-e089ef5070dc | -5.16904 | -56.04324 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b8991f5-ae21-308b-b988-70b5f1d62b23 | -5.30673 | -56.01821 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b94f3fe9-a32b-3f81-9166-f25a0f9abb17 | -3.97446 | -55.70871 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1c578ea-c69f-3227-8c50-a0d82c9937ef | -11.28048 | -45.70282 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e295fe7d-35c8-3495-8040-926d0d60f0e8 | -11.28788 | -45.70673 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd7b5949-dab4-3866-a589-a9be7b51bc05 | -5.33441 | -56.02633 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 320c9704-6c80-39df-a4fb-5b10ed3a9b64 | -3.20003 | -61.23199 | 2026-09-06 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc4db5cc-a359-3bdd-ab5d-c53a1a2d35b8 | -5.31194 | -56.01179 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db971157-6366-3bc0-ae01-638430fd51f6 | -4.77629 | -56.11901 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a5c44fe-d324-3978-96a1-afb99daacea6 | -8.97327 | -44.40413 | 2026-09-06 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1aa409d8-b625-3495-8a2e-942b1f45eccb | -3.86069 | -51.04137 | 2026-09-06 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 222bd8da-ddb5-347e-afbd-3bf6967c19bb | -3.80788 | -55.88495 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81d316f4-f491-3504-bf6c-056299078d7e | -5.37132 | -56.02881 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8aefbca9-6558-347d-bfe3-f3d7243c3b4f | -4.67897 | -55.63377 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 919fd28c-2843-37ba-bc8a-24de4fe23a69 | -7.36878 | -47.02103 | 2026-09-06 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05ff6983-9a45-3d53-bf40-35047232b435 | -5.35057 | -56.02897 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abad393a-6b4d-316a-9ff2-4de0b45d99e7 | -5.36556 | -56.03877 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e057ace-d1bd-31e8-8295-04c4cce99f41 | -11.29293 | -45.70272 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0349c6d-dead-31a7-9363-879fe94f99d9 | -7.10524 | -56.5118 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac42a781-8b54-32d1-83a4-296b37bc3bc9 | -6.25835 | -51.84656 | 2026-09-06 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eec5e79-e3a2-3fad-84ea-a884407dcbdd | -3.19929 | -61.2363 | 2026-09-06 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29210bd4-d6ba-3207-8583-efb828e7c443 | -3.21778 | -53.16932 | 2026-09-06 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2816ab4c-e0ce-3e6c-a76a-23521dc9a042 | -5.13948 | -56.26973 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2b1762b0-1270-32e3-a67a-5d4966f41d38 | -3.78389 | -58.85427 | 2026-09-06 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8da9d09f-d110-39e1-a2ad-f62779b517fa | -11.28509 | -45.10715 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c518a53b-0d89-3a28-8c82-adb7d2ac155c | -4.46863 | -55.09542 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 847c70f0-b880-3476-8d40-76ae81634c21 | -5.96714 | -57.6948 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f81dbd99-0161-3d05-94f9-6bfc8ab4884a | -3.68102 | -51.25452 | 2026-09-06 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdbfda17-dbe5-33a5-92fa-0abd8b110439 | -3.7022 | -50.02916 | 2026-09-06 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ddb0f09-b10a-3b2f-af15-7fbe82b04c3d | -3.82571 | -54.82926 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2876acac-9602-38e9-ab33-86eb3192c82b | -3.55 | -48.18208 | 2026-09-06 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e4fe7571-b9be-3244-a31b-0548d4a39a7f | -5.34307 | -56.02408 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 010f6438-533b-30da-a58f-12ef0e48fd98 | -5.25122 | -59.97856 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33284c9a-b6c1-33cf-9ce9-b57f1f1fc06d | -3.85792 | -51.03741 | 2026-09-06 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf72c9a7-800e-341f-952b-e4b97146a701 | -3.55406 | -48.17881 | 2026-09-06 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| eea1e479-4d28-37b5-9eed-8937c6983110 | -5.13536 | -56.26907 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 2bdfc927-5fe5-3758-aec4-fb7f3cac69f4 | -5.29019 | -60.13144 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92305dce-7571-3081-99f6-f9aef7083914 | -5.14961 | -55.95457 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1381b549-72e1-38d7-b7c9-dc2aa4c24a8a | -7.89737 | -47.69995 | 2026-09-06 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8af4c35c-6f9c-399f-90a1-4287282a8db1 | -3.19602 | -61.23304 | 2026-09-06 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6493f9d2-50ce-3f2e-bf3d-52ee99ac61e6 | -3.2251 | -50.2971 | 2026-09-06 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07661a5a-31d0-3fa9-863f-1879edbfdd05 | -6.08987 | -55.59024 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa6de134-7676-3321-b29f-dd022100af24 | -5.69614 | -44.49252 | 2026-09-06 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5f37cbf-32cd-3b10-b7e3-11521952b8da | -5.30387 | -56.01045 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6c1b5ed-4ef4-3118-95c1-e1b55380acb9 | -5.37189 | -56.02525 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |


[Clique aqui para ver as próximas entradas](README19.md)
