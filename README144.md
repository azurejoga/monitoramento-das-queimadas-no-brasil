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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af393747-6a3e-3066-a960-ec0d34216c04 | -3.53404 | -59.57373 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 45488b88-4291-3718-8134-67723fb224b7 | -11.99512 | -43.48982 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f20c8d4-e952-3b85-b2b5-025a17547db6 | -5.6901 | -53.49178 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cc657a9-add6-3d26-a5c6-4a3328ff8ad3 | -3.4507 | -59.54704 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e588e1a5-7c80-326f-b465-b4a923989e5d | -3.73517 | -59.45787 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a6cc6655-3cd7-3eb3-adaf-add4206d1082 | -3.03933 | -54.1441 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c933c3e-f05d-3ed6-ace3-060bdc1a318a | -7.08492 | -52.67654 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbea4b95-a44b-3afd-a081-2ab25254f6a9 | -3.00124 | -54.11127 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59fda7b4-3d76-3315-b90e-fa0dec22a318 | -6.86146 | -55.7884 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cfafbad5-dd89-3033-81dd-696bb0166460 | -4.74505 | -55.67797 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| e5c6117a-8c7a-38b4-8567-a20de07595ba | -6.88689 | -45.89209 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6fac1c2-0cf3-3c69-82f1-5918fb7afcd1 | -2.94143 | -55.79171 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f82d168-662a-3b3d-b833-45759cc9d965 | -5.96166 | -55.36216 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9c72399-6d86-3026-9846-3a090b48e9ae | -11.21977 | -45.31568 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5b561bb-b935-3a5b-ae2d-36f3bb21b53c | -2.9363 | -54.18031 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d84d97f-1597-31e8-b4eb-cb2995f3f59b | -3.01112 | -54.05277 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9635302-f0ec-3ebc-b817-b1abc46caccd | -5.8889 | -57.72461 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05ee6093-968b-3840-b300-f72b9b74831e | -3.17747 | -54.74211 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6824b388-a0e7-35e6-8f65-8428fea969f2 | -11.22251 | -45.32193 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 46b5c68c-d66f-3907-94a0-42541986f824 | -5.09829 | -46.20639 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb9d31d6-3add-3b68-abff-8909d3491802 | -3.0069 | -54.05298 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45cf3598-8adf-339d-bb87-5233f7788b93 | -3.90953 | -55.90117 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e03ac4cf-ca8f-382e-b277-e7ab92d07107 | -4.09333 | -48.96266 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd29e7d1-0aa4-3644-9db6-2bf599f4354d | -11.60927 | -43.70944 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 707776b9-bb8f-3098-9ca5-d1637f199431 | -3.54157 | -55.52892 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 298fcc09-b7e5-3e5c-b9c2-f8cd06c41d1e | -9.20949 | -60.8675 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55eaf1f7-ab0e-3d9b-8258-5f3f1b38f460 | -6.18826 | -52.86864 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfe2c2ea-dc2b-3c34-a1c2-7e926838ec2a | -3.00898 | -54.24276 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80743166-1058-380a-b81f-c2fc9a4f3507 | -4.2903 | -48.56028 | 2026-10-09 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bc636e3-8143-3123-b301-40bc150cfc07 | -3.03593 | -54.0764 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 157fe820-f6cd-3d98-bb35-be9411a9770d | -11.86345 | -43.56501 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30f10521-6568-382a-8c4c-d24feba803e1 | -11.82483 | -43.58864 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 09cea8c7-ef55-3c2a-9247-0252a3f046d3 | -3.00333 | -54.12252 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07ff1d0e-f7e3-3ed2-8a76-5e6504cd8681 | -2.93235 | -54.04898 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 430852d4-53ef-31ac-bfea-be7451d6a036 | -11.07523 | -44.08921 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 191cfbb7-f157-3456-8d6e-592f3444827a | -3.00212 | -53.90368 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1958f217-ea42-335d-b043-33c51c1d2753 | -3.70312 | -61.32716 | 2026-10-09 05:04:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6c4310b-fd36-38d3-a406-de8c2cbc27dc | -6.51419 | -47.39124 | 2026-10-09 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a14e1f5-741e-35a6-a462-41d3cf591ff5 | -2.58505 | -56.17989 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1e106f0-5a20-368c-b319-14daa0d558a9 | -2.99608 | -53.85258 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16fe9e1a-e9b1-3946-9fb4-22963af33ed7 | -3.10573 | -53.93104 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da877108-4689-31ec-9928-b4eea81eb318 | -3.65244 | -54.5256 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddd52593-1de5-3d53-856c-ec484afa69fb | -3.02345 | -54.04296 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 870e09d0-b4a9-3717-8f32-b94c82550a60 | -2.98601 | -54.11677 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2193a8d1-160a-348d-b7bb-69605aab5ff0 | -3.69502 | -55.4847 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbf8f050-0090-3761-bde2-9afa7f840038 | -3.10434 | -53.962 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 746113e6-2123-3827-8d42-91a267bef720 | -5.09092 | -46.21916 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93609dbb-f37e-39a4-a427-e1dad20c732a | -7.30038 | -46.16008 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d38f0ad-f857-396d-a7f7-44e9c443447d | -3.55674 | -59.46903 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e97055e-0b31-3f7e-b249-16aa66c9887b | -3.99198 | -59.35477 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8c643e95-1d47-39ce-a2a5-13feb4a42682 | -6.49212 | -55.30396 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 172cce9c-1047-35a1-a18f-f9d5d546dbae | -3.29481 | -54.05714 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec745398-9e54-375b-a278-2fcd0e69fa21 | -3.08724 | -58.09481 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90e544ee-1a69-3090-b2f4-c33d4addc2cd | -2.99804 | -53.90692 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e5f6b78b-7a7a-3ff8-b37b-a4fa2ff13035 | -2.70548 | -57.46613 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbb66638-ee71-39da-b1a9-f7169c8e3caa | -6.88234 | -45.89145 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f96bdf4f-8233-3c54-ba67-f406f431c068 | -2.98454 | -54.08096 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b6d23bd-d2ad-3553-b118-f8ac43f31680 | -3.02545 | -54.18555 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7c070699-dbe1-357d-8b7e-e5e6238167be | -3.30619 | -53.70028 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c5d81b3-c2e7-3eb9-9a67-04e65a15b627 | -3.4144 | -59.57141 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 60f86669-af3e-3327-8165-21ef3b0749ed | -12.02482 | -43.44519 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b6b61af-5db1-31f3-95be-04798aa7eed9 | -11.06234 | -44.05851 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b99d9cfc-9c4c-3989-a489-6f889549cf7d | -3.1806 | -58.84394 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6241926-de4c-3166-a4c7-6cff0a58670f | -3.82607 | -59.41108 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35768ad4-da0e-390f-bf8c-d58fbc3a7a48 | -6.39295 | -55.26268 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 602680a1-f632-36c0-8e5f-f4e8934e1af6 | -3.2958 | -54.00653 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ca71d8e-5ee4-3f4e-9035-09401bfd0322 | -3.74136 | -59.4804 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e87363c8-d0dc-3e85-8107-a88fa613cdcc | -3.2903 | -54.04078 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e071237-4c28-382a-818d-b4aaadb9319a | -11.41497 | -47.58783 | 2026-10-09 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0564bb59-5683-3c6c-a8ee-70c3a7137e99 | -2.57245 | -56.18299 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 061a54c8-6df7-3e77-a25d-2912dea74ad8 | -10.8887 | -48.51016 | 2026-10-09 05:04:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41551bce-d953-3fc4-b794-f4859466b368 | -3.53869 | -59.40535 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0d002b67-cd01-3439-9f5e-2fa6f89ee3d8 | -3.89808 | -59.44586 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac8ed72f-b3bf-3e1a-96da-2c79e4f1a370 | -11.66554 | -46.77598 | 2026-10-09 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00e9daea-ca59-32af-9e4d-61cf3ee94ac6 | -6.45015 | -59.94881 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c24d4556-9901-357a-944b-ff3f770d26a9 | -6.3098 | -54.80353 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69468020-4f2b-3f7e-8130-9480af05760e | -7.25403 | -48.06538 | 2026-10-09 05:04:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 469bf198-a35c-3f99-9b7e-fefad4d47b78 | -2.99896 | -54.10301 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b5f9106-2eb1-35bd-9acf-a218ad9656e5 | -3.03232 | -54.14302 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf8612b8-8b56-3a08-8b4c-725bef86f7af | -2.99579 | -53.89878 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd5223d4-4678-3127-956f-f33e9dee8031 | -3.28724 | -51.53875 | 2026-10-09 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ee10a10-f007-3dd9-b17f-3ba990b8b446 | -7.40803 | -44.75549 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 381cb83d-4460-344a-8489-2365f9aefcd7 | -5.09524 | -46.21986 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a13baa66-aae1-3a59-98e1-542ad6708aa2 | -11.21698 | -45.25983 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b9bbb96-824a-384c-a4be-2719c0aad3ab | -6.48791 | -55.30738 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae4c0e67-9e71-3e07-bb68-3ea4981eb8cb | -4.94194 | -45.66526 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd3a0329-b799-3b8f-b480-efa1cebecd95 | -3.05443 | -54.02833 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf9f2c95-d9ed-3202-b353-0a72637b20f5 | -11.8372 | -43.58247 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6496e79-64c0-3144-933e-b29ac1d8e439 | -4.66703 | -49.2316 | 2026-10-09 05:04:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edd9c801-8595-34b8-82d7-47c5d63297cc | -11.64106 | -43.70238 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a90fc64b-5522-361c-8da0-0eb3fa51f49e | -3.03837 | -54.23944 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c399741-50f6-380b-ad1d-0fd6f96936d8 | -6.23927 | -52.88366 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d62ccec9-e7db-3281-85a1-22efb7811d22 | -5.69291 | -53.4958 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2b07e21-1835-3473-8e87-9e7638b8bb0e | -10.97555 | -45.39337 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 893d2deb-5bf2-3932-a804-fe184c1c18b4 | -7.81697 | -49.21993 | 2026-10-09 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55f3de47-7588-3ea7-aa1f-b865d0a8d931 | -10.43159 | -47.30766 | 2026-10-09 05:04:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f383f1fc-93f6-370c-b330-8a0c209ba249 | -6.30533 | -54.78696 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3366f5d5-706a-3cc8-8bdc-4755a8b35b21 | -4.08909 | -48.96622 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b8bd3d-b24c-3490-b651-89338caf7e2c | -8.84339 | -45.42376 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 962428a2-98d6-3eb9-8dee-89203fee07f7 | -3.77629 | -58.58399 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README145.md)
