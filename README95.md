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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24fce742-11ec-3e85-9ca7-cfbeb079ac47 | -3.46831 | -59.53428 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 440e1441-7c55-3934-b808-1c91553f27a2 | -7.1949 | -46.55545 | 2026-09-22 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b2680d6-11c2-3838-b963-429edf443e56 | -3.22821 | -53.94973 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 45608ec8-6fa5-3e8e-aaf8-cf9f3b1ca89c | -6.74941 | -59.42049 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc505636-54ed-3c19-94ba-3d277821454d | -6.62913 | -59.92854 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 88c1b64d-6146-3c00-b267-d3b2d5e0e467 | -3.06157 | -54.41722 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ccd5087-1b17-301c-8543-086eaf8d1562 | -7.58534 | -57.6829 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 815c4927-3034-3be1-ada1-76eac94f4d17 | -6.22365 | -56.04068 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 374b5dba-2bf1-35fb-9abb-1cb7dc132bb5 | -3.36394 | -50.76785 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 141f9ee4-ab86-354d-a649-1470867089a9 | -4.3905 | -55.04223 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eb763df-b396-3ecb-b1f3-53fe57b425b4 | -14.91613 | -49.89906 | 2026-09-22 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d31fb2f9-50d7-3672-a76d-9e2bd399e50d | -11.01264 | -54.14788 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8285e33b-214e-323b-9b66-86f65d8d7bf6 | -5.91806 | -55.6945 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3db52f6-ad7c-39e7-8bf6-7c8d06aaa4ae | -4.508 | -54.96171 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84b0be86-1e87-37e2-b388-00f3fffe3e13 | -3.01046 | -54.16682 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bde439df-bcdb-3a4c-93ed-6a12cfa20abb | -6.76507 | -59.11132 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc76c999-98de-3869-b338-2eb702d2db0d | -6.06162 | -57.86137 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a05ee0c9-3373-317b-bef2-68c8d5472563 | -6.5305 | -55.3619 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a19ef9d1-49e9-39b0-87c4-6a8a614f987b | -6.62337 | -59.91951 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 11f3025c-a177-313c-8ad4-5ecd24084b2f | -5.8796 | -53.63764 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5d38185-f104-31d3-8228-5160af74fc0b | -5.87018 | -53.64959 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 031a0dfe-4766-32be-aee1-6bbf59a5604d | -8.14678 | -54.81378 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac84bc59-414a-350b-8734-8c9c8b2ee863 | -2.87593 | -57.79379 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea9b5dd6-49f5-305c-ae2d-4b234a2cd8ea | -6.30684 | -57.74649 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd509948-55ab-35ba-8e1b-9e694d060252 | -3.21212 | -53.95979 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7d10196-26c4-30bf-ac08-0a9e3972f9ec | -3.63615 | -58.91522 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 542e7f2f-484e-3e85-97a7-2d12d700d36b | -6.62625 | -59.92402 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5494b7be-8765-3261-8699-b2ae84320612 | -6.77936 | -59.00101 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcff2aaf-17ed-3b42-831c-6d05a75e8d40 | -7.59088 | -57.66951 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc0b00a7-55cd-384b-b6d4-315619a37a27 | -5.1985 | -56.07529 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28178067-ff4e-32e1-9cd7-e5b311bced40 | -13.71494 | -48.78696 | 2026-09-22 05:23:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdea6a39-c985-336a-ad77-4a9a86e7fbea | -6.12888 | -55.81875 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5ecf4b2-9a07-3165-9a2e-36f3fd475c4a | -6.70898 | -59.00458 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30d5cf3d-19e8-3e27-bd42-0852f2c83033 | -4.35061 | -55.49939 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5790f30d-c4df-3188-90bd-27bd4d35c427 | -4.4293 | -55.08257 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2dc6be2-05f4-31d4-b8dd-741071e24ced | -4.41504 | -55.24191 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f288cffb-935c-3521-a8fd-5b9cd7c04c6b | -6.74361 | -55.09329 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c78871c-dcf6-3cfd-a73d-f7fcddd282ef | -5.80794 | -57.73851 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26c2036d-081e-30d6-a908-240995d8e623 | -6.22991 | -55.43607 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b146a4e-a049-3ac8-ab75-62c34c0dcf45 | -5.88479 | -51.57565 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d4c4a2f7-2710-3107-8832-839619dd7912 | -5.87011 | -51.93758 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea563518-8b5e-3bca-85c3-6eed1095c0c6 | -12.87227 | -50.94291 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3410d5a9-b3ba-3609-ace9-27309779279d | -12.33885 | -50.67249 | 2026-09-22 05:23:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92d92fe8-e112-3754-af56-8f23911d74b1 | -3.05989 | -54.40523 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5510812a-fbc3-3f45-a893-3e0861f8eab9 | -3.7804 | -58.84441 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c71826c-3643-3065-9232-0e6e595d1ee7 | -9.62692 | -43.94062 | 2026-09-22 05:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 832741ef-da89-32d9-931e-4985078d23c6 | -6.06662 | -57.87291 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc92820d-affe-36a6-adf0-1723f17be297 | -1.39136 | -49.32508 | 2026-09-22 05:23:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d1dac974-cb94-3041-b95e-96e3427161f9 | -11.69873 | -50.98809 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| c8b828a6-0db6-3399-88c4-d6df82603d8c | -5.20467 | -56.10159 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4f61f24-c12a-36e1-b5d8-2fe26f61a401 | -3.51043 | -59.58134 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0ee2d58d-fd71-3f41-b4aa-3e9e577cc2bc | -12.95612 | -50.92709 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e1b9c0a-9a7a-3e85-b641-c419141b0afb | -6.35588 | -58.29026 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 153c59e0-0c6c-3097-8c5c-5cd9cfd513e2 | -3.92996 | -56.04732 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec8caab8-c14e-356e-85c8-af8ca67bef51 | -8.79153 | -44.27165 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| cf9498d8-7d89-35f9-9d26-8b5485f760b5 | -13.51658 | -51.5235 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| c92d2c52-b23a-3ce0-b690-efcf1c32383e | -2.27859 | -57.99492 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0318d7c-7fdf-342a-a7db-f5b3e68f7491 | -3.34265 | -59.85518 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ad6c8d3-713d-36b4-9599-2a684775bef6 | -6.75172 | -59.06406 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5266850e-b597-3740-8fa5-0e8c59dabdaa | -6.43252 | -55.61457 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5e76c2b-c74d-353b-8204-b4d1a880ea2f | -4.68272 | -55.62734 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11731627-ad1d-31a7-9aed-14bf081c0b36 | -11.99543 | -58.07114 | 2026-09-22 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f61ba881-d157-3bc7-b1da-53ce103adad8 | -3.5514 | -58.54902 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 929ba7ad-60b5-3a88-9855-498ea5758c41 | -12.77152 | -52.84904 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e7036d1-a4b7-39c9-97ed-e8384dd9ae8f | -10.46949 | -69.19559 | 2026-09-22 05:23:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4161b1b7-7e7c-3082-9d14-a72ae9d1130e | -8.14862 | -54.80147 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a69f689-4b4f-3510-8bb6-466f177f0281 | -9.09966 | -65.36935 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de60794c-1782-3360-8285-7383da22146f | -10.10213 | -69.12955 | 2026-09-22 05:23:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93c59a6a-bf99-3c4d-bb52-c93d8fdb5a48 | -14.75165 | -48.43752 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a7fcced-3ac6-3ada-92aa-34bd37f0516b | -3.541 | -60.57848 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3006890-c2e9-3b36-ad33-edd94e27f396 | -6.88936 | -59.07862 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f391d97-8102-3a5c-9f46-7411439ffb28 | -9.6208 | -43.93902 | 2026-09-22 05:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c6725275-0d70-3ac5-ab0f-a7a4fdd30555 | -5.82182 | -57.73715 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f26dd9c-4e60-3fc8-9f63-f3ec893fd429 | -1.29808 | -54.20492 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b653824b-f178-37eb-a1e7-b3d37b75dcb5 | -6.68725 | -59.15896 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cde89f0-9419-3659-86b4-2080c24d3de7 | -3.9072 | -51.88823 | 2026-09-22 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4caeca3e-d76b-3f5d-abd1-778f8c8eb8de | -3.93657 | -59.64559 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3447df26-4684-35b5-900d-29dcf258b0d0 | -6.45812 | -49.87815 | 2026-09-22 05:23:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de62a81e-9bb8-3deb-a428-a666f5b74e79 | -11.00685 | -53.99771 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35c81c40-81f6-398c-afa0-c8cdb066d172 | -7.24708 | -55.58506 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b06b9527-a50c-3ce6-8911-76cdf5209ad9 | -14.75744 | -48.43952 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dfeb9c6-0a5b-3ecc-8455-c51d38cd0e26 | -6.9296 | -59.63128 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58a2953c-18ad-3940-abf2-7b1a49994384 | -3.68497 | -60.59478 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79f358b1-5a20-3478-b5b5-fec442fa2860 | -3.23113 | -53.9543 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f2f9bc2d-d336-37dc-92f5-1e52b6177aed | -3.40958 | -61.29891 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74106cb1-915c-30ca-9100-5bc91f1e02df | -3.34059 | -59.86776 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a46c3bae-9a5d-3927-be46-12a873f1262e | -6.67185 | -50.94028 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8609795-f42c-3a44-a48f-1859c73b51ff | -8.67299 | -70.03272 | 2026-09-22 05:23:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e25190a-f325-3191-9a05-6f60b6ec588a | -6.52014 | -55.38342 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc9e117a-1142-3b48-9b66-11e7ef05b69e | -6.90412 | -57.61049 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd22cb63-67a5-3975-884d-f4fb7ff004c2 | -1.32345 | -54.65992 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bb4ce60-a567-3456-bedf-4e692937a5e3 | -3.12822 | -61.43412 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04a389ef-1231-3fbe-9a2c-1a3304bbbdd3 | -6.39044 | -60.02079 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 172b26ca-5046-3ff7-b7dd-dfec7c1983e9 | -3.01029 | -54.19062 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1fd3f940-f6e6-3d37-8bb6-3cbe1e70f3b2 | -3.0109 | -54.18677 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e08a336e-531e-3864-9df7-aa4bac6c486c | -2.99894 | -60.8006 | 2026-09-22 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f41be3ab-e436-3bc7-a9fe-9532bd59b341 | -3.01274 | -54.17515 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc027ce0-b969-3ff8-99a8-1d54d888a9a2 | -13.02261 | -50.59416 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3931ab15-0ffb-3fc5-9280-af8bd21e9bd5 | -4.51138 | -54.98512 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74d836f6-08ef-3465-b31e-b2a562849cc6 | -6.64447 | -59.92301 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |


[Clique aqui para ver as próximas entradas](README96.md)
