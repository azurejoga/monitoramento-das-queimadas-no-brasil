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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cd4b683-2879-308d-a65b-b855f409549d | -18.05862 | -45.17878 | 2025-08-27 04:06:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52c5ed09-418a-336b-8fc1-842c8572e30f | -18.28999 | -40.99906 | 2025-08-27 04:06:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1d5504f6-589e-31e1-baac-7fb56e45a338 | -19.07932 | -48.14596 | 2025-08-27 04:06:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75a87f23-06fa-3a8f-a1dd-02811473f654 | -19.05786 | -41.91003 | 2025-08-27 04:06:00 | NPP-375D | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| aa8ee44b-f536-3141-a198-521ea613b2f0 | -20.14908 | -44.21091 | 2025-08-27 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d57429f9-9e49-39e3-a4e4-d65148261d60 | -16.84145 | -43.85279 | 2025-08-27 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b243a216-96dc-3766-b869-7f0775ffdde1 | -19.0612 | -41.91061 | 2025-08-27 04:06:00 | NPP-375D | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 462189ea-f882-36c5-8a83-6c02ec31481b | -18.21871 | -44.52861 | 2025-08-27 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19a8b2ce-c9dc-3a87-b8d7-a59b12476af5 | -17.97375 | -48.04886 | 2025-08-27 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de6bb35b-53d0-34e5-ae9b-119f41f536e5 | -16.92494 | -49.44061 | 2025-08-27 04:06:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 892c3e03-d78e-3ba9-8adb-4f48926b438d | -18.08002 | -44.05723 | 2025-08-27 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb88427d-823b-3e01-9c7e-38a329c16854 | -20.51909 | -42.27168 | 2025-08-27 04:06:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4f90661c-ed7b-3d61-9e31-8017003c8d98 | -19.90956 | -41.58361 | 2025-08-27 04:06:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| faf9b1ed-2924-38b3-902e-9e512f7ed8ed | -15.6268 | -52.73346 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9463bd48-578e-3d8d-a9bc-79cea72f6c0b | -15.6219 | -52.72814 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 421c2722-ac52-3f40-ace5-5fb4c6b2a729 | -20.49159 | -42.97057 | 2025-08-27 04:06:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f82a77c7-c20f-38e6-8f3f-4c12a38534e2 | -20.3717 | -42.19311 | 2025-08-27 04:06:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 33fefd57-c26b-300a-96cf-2ef20f59cd78 | -19.46372 | -44.18962 | 2025-08-27 04:06:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cb56421-6ed7-3c5b-89d8-3c9d7b1dc5e1 | -18.15155 | -44.42358 | 2025-08-27 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd9cf05e-a6d3-3e92-a013-c4adc20483b1 | -20.65234 | -42.45422 | 2025-08-27 04:06:00 | NPP-375D | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b216eaa7-c5ad-34c1-bd41-52c9fa20809b | -17.71268 | -44.39046 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cde680ee-22ff-348c-a861-cd638381366b | -18.22936 | -44.52233 | 2025-08-27 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a210658b-fb94-361e-af51-949d96b2ffcc | -18.15294 | -44.43621 | 2025-08-27 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9fa7642-a2d6-39e1-9a5b-75309afc816d | -17.70278 | -46.06335 | 2025-08-27 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 908d7526-b70a-3b30-859c-6534b2132b33 | -18.49084 | -47.23278 | 2025-08-27 04:06:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deeee634-504d-349e-b0e1-447832f32350 | -17.81119 | -44.51322 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e99f894-eebe-3314-8fd3-f7d50aab7dd7 | -20.11231 | -44.32817 | 2025-08-27 04:06:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7eb5a9c4-fb19-3657-a045-0e79ff66ecbf | -20.37114 | -42.1968 | 2025-08-27 04:06:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 49be16bc-191d-3188-9dc3-71ecf928c891 | -15.62281 | -52.72382 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 641f520f-44fe-3f73-873a-75fd9bfa2000 | -20.11295 | -44.32437 | 2025-08-27 04:06:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a4696d07-3d03-3081-b7a0-1e2aa13fda4f | -20.52301 | -42.26854 | 2025-08-27 04:06:00 | NPP-375D | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9a5f80b7-960f-38af-a312-8b9b0a35c749 | -19.08063 | -44.32806 | 2025-08-27 04:06:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44b67039-2238-3cfa-a96f-ea25ef514eca | -19.69621 | -42.11134 | 2025-08-27 04:06:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 93622a02-615a-350c-b87e-3634966b5731 | -17.25935 | -44.88422 | 2025-08-27 04:06:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 41ef8a91-66cd-3aea-a797-3ac9c66f3f8c | -17.80906 | -44.50482 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fdb1434-a235-3834-8424-644264c6e966 | -19.02498 | -43.88358 | 2025-08-27 04:06:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f7a55b0-825f-37b5-8b7e-3d340239271d | -20.03127 | -42.11793 | 2025-08-27 04:06:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 575436e9-6e13-333c-a1b1-3c5628814c73 | -19.97891 | -42.04736 | 2025-08-27 04:06:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 84c496b2-45cc-3dcb-a458-55e1f34ff981 | -20.05849 | -42.60064 | 2025-08-27 04:06:00 | NPP-375D | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5dd36971-e13a-339d-8ea9-95b9df97fa47 | -17.97636 | -48.05766 | 2025-08-27 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e33d89e2-57fe-3293-aaa1-d6c7584d150e | -18.92904 | -41.93433 | 2025-08-27 04:06:00 | NPP-375D | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 09f8afb9-4117-3b39-aedc-0530b6b012dc | -21.00786 | -44.17805 | 2025-08-27 04:08:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74d3533e-1589-3d49-a017-26342f719047 | -21.38424 | -46.93534 | 2025-08-27 04:08:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 663e76c0-3605-3fc7-b91f-6034728cb47b | -22.16555 | -47.07298 | 2025-08-27 04:08:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 606e7fe0-5af0-3698-bde9-d8d5d5323427 | -21.13774 | -45.88732 | 2025-08-27 04:08:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 21fa59b5-6f3f-3469-9035-fe320e2e5995 | -21.13144 | -45.88181 | 2025-08-27 04:08:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| aeab72c3-5f31-3f56-a265-8830bde69ee3 | -20.75773 | -44.75619 | 2025-08-27 04:08:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| c0a91d1e-9862-3433-ba6e-5bffc8a6ee6a | -21.13769 | -45.88567 | 2025-08-27 04:08:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 9de36e40-bda9-387a-91be-4e94203982e4 | -20.39579 | -46.72739 | 2025-08-27 04:08:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65b49eb6-5c98-3fba-a167-0473cfa85966 | -21.34793 | -46.89246 | 2025-08-27 04:08:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| afbc0d58-9d85-36e9-9a07-4a2abe03d680 | -20.40108 | -46.71906 | 2025-08-27 04:08:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 17a749a4-9a8c-3574-86f8-50c3ff6a4a2f | -22.18341 | -46.63412 | 2025-08-27 04:08:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0feee253-ef35-363a-8c00-25a4e0501b8c | -21.35968 | -44.22653 | 2025-08-27 04:08:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6bce61c6-e706-32c1-8ace-f34cbf0c64dd | -22.65484 | -46.25407 | 2025-08-27 04:08:00 | NPP-375D | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6c9a3e1-d8eb-3225-baa1-6803da448922 | -22.02075 | -42.20897 | 2025-08-27 04:08:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ea53b807-4a9b-3081-9e06-758299d66964 | -21.24102 | -44.58338 | 2025-08-27 04:08:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7ba394b3-3cd7-3196-944f-8906fdf7726a | -20.79781 | -44.57761 | 2025-08-27 04:08:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d4fb6532-e2be-330e-8ef9-89dd3ed52351 | -21.66206 | -42.34857 | 2025-08-27 04:08:00 | NPP-375D | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e8bd29ad-664f-3990-bc76-1eaf7f51da72 | -21.78787 | -43.3018 | 2025-08-27 04:08:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1b295880-ea30-3cb7-be23-10b8a0120ad5 | -22.55268 | -49.76685 | 2025-08-27 04:08:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23168b86-e64a-3f50-bd40-c60e2ff53ae1 | -20.98954 | -43.30754 | 2025-08-27 04:08:00 | NPP-375D | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8d1b6e85-a8ef-3644-8a1f-a2f9771c939f | -22.68756 | -46.83476 | 2025-08-27 04:08:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c784e88c-eda7-35ec-b8c6-0991318fda3c | -21.38342 | -46.93984 | 2025-08-27 04:08:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ce08ed8d-87fb-3947-a342-533316254a31 | -21.38525 | -46.93803 | 2025-08-27 04:08:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| dcc3fb20-2f3c-3903-8424-80d6128ebcbd | -23.04232 | -50.31965 | 2025-08-27 04:08:00 | NPP-375D | ANDIRÁ | PARANÁ | Brasil | 4101101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e261c064-1781-38aa-a465-84767b8ae457 | -20.40026 | -46.72364 | 2025-08-27 04:08:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6c74915e-e78f-3f88-a568-e8b04a670b3f | -21.38036 | -41.99685 | 2025-08-27 04:08:00 | NPP-375D | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 25493cb4-4c45-3528-aa73-66bc511a71d6 | -21.35078 | -46.89769 | 2025-08-27 04:08:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 96115434-84e0-3bef-9c27-eaca7337e921 | -21.13423 | -45.88668 | 2025-08-27 04:08:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| ea558000-9b25-34f7-9310-308f7c2c0a11 | -20.39216 | -46.72643 | 2025-08-27 04:08:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f959851-1ea7-3605-afd8-f8977d39c237 | -21.38375 | -41.99739 | 2025-08-27 04:08:00 | NPP-375D | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 45118887-2798-38c1-b020-b30a640dbbaf | -21.35158 | -46.89321 | 2025-08-27 04:08:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0de751fc-5178-3783-bdaa-b1041013f427 | -22.67963 | -46.83764 | 2025-08-27 04:08:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 23d2c7b3-4a32-370b-9b03-197a46cc41bf | -20.39463 | -46.71266 | 2025-08-27 04:08:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a52712de-bd45-31da-9b3a-9cc241b984a0 | -21.13495 | -45.88245 | 2025-08-27 04:08:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c2047548-db05-3df3-81a3-87dfeb9c9f84 | -21.7912 | -43.3024 | 2025-08-27 04:08:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 47700db4-ab2b-392b-9e44-ee806a6db817 | -21.72246 | -46.80731 | 2025-08-27 04:08:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8afa5423-dc37-357f-ada2-7b4e6c61d53a | -22.45863 | -46.79584 | 2025-08-27 04:08:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79485d42-97f9-33f5-9c8f-2030dbf9a970 | -21.00452 | -44.17742 | 2025-08-27 04:08:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e71542de-d286-3a60-9793-a206c181ea7c | -22.68398 | -46.83399 | 2025-08-27 04:08:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1a28271d-011b-33ab-877d-bddd551a6094 | -20.52644 | -46.11409 | 2025-08-27 04:08:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed0a574a-2562-3f77-a173-e0be4e4c07a7 | -20.98895 | -43.31124 | 2025-08-27 04:08:00 | NPP-375D | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 52204c4a-6e39-3e4e-8895-8a95215da678 | -21.2404 | -44.58717 | 2025-08-27 04:08:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6d56b788-f805-30ce-a3a7-8a52342886cb | -21.00179 | -44.17304 | 2025-08-27 04:08:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 44da6540-e89a-3159-81af-59f28ab158ae | -21.23703 | -44.58652 | 2025-08-27 04:08:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7e4f10d3-616e-34fc-a9aa-f148c7d25436 | -21.13071 | -45.88607 | 2025-08-27 04:08:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 4a99ac52-5eaa-3111-892c-04f76c2e47bc | -23.07966 | -50.4028 | 2025-08-27 04:08:00 | NPP-375D | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ba1fd4b2-c632-3533-99bd-f606db4ab799 | -20.40471 | -46.71996 | 2025-08-27 04:08:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c60c5fdb-e250-3158-8e66-790cc5a8cae9 | -20.39944 | -46.72821 | 2025-08-27 04:08:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54e4ebef-349d-31b8-afd3-719da37c84d0 | -20.75709 | -44.76003 | 2025-08-27 04:08:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| a0358530-dc64-3875-807e-4840c327cfa0 | -20.39827 | -46.7135 | 2025-08-27 04:08:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a7349838-5606-3190-8700-03c2a2945c79 | -21.34713 | -46.89693 | 2025-08-27 04:08:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8f13d46b-f3a1-3746-8f6d-57d0eab917cf | -21.43151 | -45.48643 | 2025-08-27 04:08:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d8caa167-d428-33a0-bcf1-ffd0c454a6c7 | -20.53 | -46.11478 | 2025-08-27 04:08:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c08cbcca-5ebb-32de-8968-81671e315fd5 | -23.32579 | -47.84267 | 2025-08-27 04:08:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 999097e4-4d87-3391-922e-cd849f90a9cb | -21.36241 | -44.23092 | 2025-08-27 04:08:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1ae7e939-c5b1-383f-91ce-e27b6cc7a07c | -20.79444 | -44.57696 | 2025-08-27 04:08:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 828732f9-c5d3-3630-928c-723cbbafdfb6 | -23.08398 | -50.40376 | 2025-08-27 04:08:00 | NPP-375D | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d1ad4814-96b0-3929-b147-ce0d5d1604aa | -21.11636 | -45.73851 | 2025-08-27 04:08:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eb3fe19f-023d-343a-b517-96b90264563b | -21.00513 | -44.17366 | 2025-08-27 04:08:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README34.md)
