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

## Dados Diários - Página 206

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e798fdaf-5278-3314-bc0e-f77016b052d9 | -6.20994 | -52.84946 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 000ecd71-1823-30da-83fa-176dd7f5d416 | -2.97316 | -57.22498 | 2026-10-08 12:19:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c5e980a8-c6d9-30bf-b34d-3a8d3f29190b | -3.98129 | -56.11937 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 94af4272-d419-3452-a83c-ba67f8942338 | -3.10767 | -53.95404 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4a537e41-7260-3660-a9e0-5b17fd0c2693 | -2.3094 | -57.98037 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 983672b0-22e4-381b-9bcb-004dd355fa6b | -1.52945 | -54.54272 | 2026-10-08 12:19:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 48822d29-7e78-3176-a961-560954ddc0c0 | -3.58188 | -54.31708 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 211dbedd-ce39-3264-aa54-f7d38a1f85d3 | -1.47784 | -55.15659 | 2026-10-08 12:19:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| bc4ea001-dc17-3fd9-8249-1bdab24de1d1 | -7.89685 | -54.71362 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5b556499-595f-3707-9be7-a48591f1b3dc | -5.69176 | -53.4855 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 62dfc20b-df0f-3c4b-b2d7-1bbee6a5a1ab | -3.69259 | -55.49225 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 385a14d5-4d1d-33f5-8f34-831910bea317 | -2.7415 | -57.61323 | 2026-10-08 12:19:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 95263444-81ad-3ce2-a781-ba018ee9c3e0 | -7.22548 | -55.16465 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c3bddc52-d156-325b-8566-d9091aa9fb52 | -1.10293 | -54.16859 | 2026-10-08 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 1a36f34c-0937-3983-962c-6610d832b1dc | -6.39012 | -52.72266 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| e9108209-52f7-3528-90c8-1a454a51e6e2 | -3.71952 | -59.33776 | 2026-10-08 12:19:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6199f098-4af2-3034-b120-201ab0b64d24 | -3.69384 | -55.48345 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f3db6482-ebbd-3798-89fa-7dd7f2f2d89a | -2.87899 | -54.20029 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a034a7cc-5b7f-364b-89b8-5000daecb717 | -11.82805 | -49.74094 | 2026-10-08 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 2a66281c-ca39-3dd1-88ae-3372ada6e3e6 | -6.21828 | -52.78848 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 672bcb9d-88c8-3681-a5d1-808dba79af0d | -6.85356 | -55.78403 | 2026-10-08 12:19:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 02fae258-7c1d-3799-87c4-64ea977ddb96 | -3.03106 | -54.23348 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ee99ffa0-96eb-310f-848d-37a051b106e4 | -2.84539 | -57.46855 | 2026-10-08 12:19:00 | TERRA_M-T | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3a7ded06-a443-333c-b612-d377e355f73a | -4.36173 | -55.64573 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 933951d5-7f8a-3c79-a757-94ee35475fe1 | -3.59163 | -54.57397 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2dacf8ab-7c85-38fb-8c53-3d97e014c89f | -3.18596 | -58.63417 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| b561ccac-b529-388a-886b-96568cd91618 | -6.26544 | -52.88794 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 8ad80c5d-1167-3ae9-b2d5-aaa725a0e7ad | -3.11247 | -53.78666 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4a762f3c-79bc-3e1e-a0b6-889528a3f260 | -9.16609 | -61.40263 | 2026-10-08 12:19:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b8a62c47-509b-3cf9-994e-8c74bdde7755 | -3.69232 | -55.95348 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c4935038-4b5e-3f6c-8394-de609d166f04 | -1.47659 | -55.16533 | 2026-10-08 12:19:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 1b3ae600-3360-37ca-b5c4-d7e989ff320d | -1.47875 | -54.64496 | 2026-10-08 12:19:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d4a20f68-c580-3d5e-9309-e46d82359f89 | -3.36657 | -58.19357 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cfe64bd2-cd66-3b29-adf0-f242225d9f5e | -3.57662 | -54.35458 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1d1168e1-0a60-3905-b992-176067a957ec | -2.98986 | -54.06821 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 3581fc45-aac8-316f-889c-f81864b27ef8 | -1.8288 | -55.03315 | 2026-10-08 12:19:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 5b3b2f88-347e-3b2f-97f0-ca211a2225be | -3.92672 | -55.85571 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| b0adf331-46ba-3306-a5d5-9ca4104f969d | -6.23797 | -52.85967 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| c99a50b1-14b3-3da6-aa5f-5b1b808c3eb6 | -5.30112 | -60.08693 | 2026-10-08 12:19:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5fd2bfc1-19d2-3d93-9ad7-921bc6893d99 | -3.14239 | -54.35945 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3af383db-c5d8-3d1c-8a29-9ad181adaf3c | -2.99766 | -54.07894 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| a4ce23de-6797-3a5e-a156-978242f16f44 | -2.76218 | -54.11129 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 3d8964ce-299f-3188-884d-723fc15b5055 | -4.00646 | -56.25676 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f5d6b88a-d562-3bc2-9fcc-2108175ad643 | -8.00957 | -50.14206 | 2026-10-08 12:19:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| cdbc74a4-a3dc-387d-9ffb-b6cf39f4de84 | -2.98852 | -54.07769 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 7294c47a-f966-3d75-9cf4-0ed826c4c175 | -5.98872 | -55.37381 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7ad75e29-29f1-3904-96e3-e2f38243b15c | -3.84578 | -55.83851 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 04d1b50f-de63-3135-a354-10f32a9f4291 | -3.58431 | -55.60506 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5202f241-e485-3639-9e2f-cbf438e0bff5 | -3.09849 | -53.95276 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 1d4d4459-8691-3045-aa9e-7fc6774df174 | -1.02662 | -53.73137 | 2026-10-08 12:19:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1ec57bb7-7824-328a-9092-0319bd6e0109 | -5.85898 | -53.46537 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 38f9c310-5b0e-378b-9a4a-97fc86d3b7de | -5.70355 | -53.4935 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 3e672aa5-4ba1-37fc-b3fc-69f957bad10b | -6.54269 | -49.86131 | 2026-10-08 12:19:00 | TERRA_M-T | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 26a6b6a1-74e7-3e38-8ead-784f37dda0a4 | -1.87878 | -53.96626 | 2026-10-08 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2f106284-1af0-3678-94fe-d6aeae96e7ff | -3.13203 | -54.36752 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6944ac5c-605b-30e8-a881-f539d9ac753e | -6.20828 | -52.86158 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| a008ec37-6a6d-3429-b50d-b33a07ac9bc0 | -10.27909 | -53.97361 | 2026-10-08 12:19:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4189000a-9f85-35d3-b9d2-7bd5c5d9ba64 | -4.35164 | -55.13222 | 2026-10-08 12:19:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a05959a7-426a-3258-998c-745752e17320 | -5.70508 | -53.48209 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 97be45c3-688c-3f6e-a4cd-d233018a36db | -2.87415 | -54.88448 | 2026-10-08 12:19:00 | TERRA_M-T | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| e23b4a69-22a5-3ca1-847b-f4dc225b0364 | -6.09182 | -53.49196 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 72aaa127-5a45-3d83-a804-737cd61a293b | -1.41849 | -55.71552 | 2026-10-08 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 3987c83e-e76a-37c9-80a1-8e75672af29c | -3.5414 | -54.66985 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 412c8c88-a8c0-3115-8527-316f84f79870 | -3.22452 | -54.30074 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 257c2f40-22c7-311c-a513-3131a98d35bb | -1.31531 | -53.13781 | 2026-10-08 12:19:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5373f4b8-a896-3605-af42-43b5eda2ac40 | -3.58755 | -54.66678 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| cfa1fee9-0ac5-30b0-8700-ca0ce81e746a | -4.42115 | -55.74997 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ae9209e-57e7-3e35-b0e3-8c7ab231c503 | -3.11425 | -54.165 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ee5b0c61-6a2d-3fc2-bc19-f9c264590599 | -6.04877 | -53.20575 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a3a1fbbe-aae4-3071-a2bf-8c876c529a5b | -11.82521 | -49.73521 | 2026-10-08 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 9ed8fa2e-891a-305b-bfe5-62f52fab495d | -8.182 | -54.71955 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 37fd6670-093f-3452-8b9d-1f57dbc88c58 | -3.47825 | -59.58451 | 2026-10-08 12:19:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bae85e94-6ebc-3aea-80aa-762e2ec0e6b6 | -5.69828 | -53.45896 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 5217451b-2f25-3615-bbc5-bd9162c7aeae | -4.54224 | -55.61136 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5984c3f7-80c4-3b40-9a99-57045ecb8a3c | -4.75062 | -55.65001 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5711dc2d-3a5e-3413-ba2d-d44c5d7fbe5e | -3.71265 | -57.21858 | 2026-10-08 12:19:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| c78ffac4-91f8-3bbf-87b9-f8d54be29b18 | -6.0388 | -53.20445 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 674a45fb-b25a-3d69-8c80-c14e2ab875a6 | -2.72608 | -57.46835 | 2026-10-08 12:19:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| b84485bd-96de-306d-b807-bda890543468 | -7.23458 | -55.09866 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| cc80c1f9-75aa-3ee9-9a8e-577d159ec11a | -3.04528 | -54.26381 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 4c6d1d0f-4bdb-3e02-a800-2ff540e65062 | -3.02577 | -53.94664 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| c2871d99-0cbf-3694-a5ad-fc404a0d33ec | -1.5557 | -52.75039 | 2026-10-08 12:19:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 15d0bb45-8de8-394c-91c9-38436ef196e5 | -5.71329 | -53.49464 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 62ed7e7c-ae58-30f4-b091-083fc61b571e | -7.38496 | -55.21144 | 2026-10-08 12:19:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b56dc998-b393-3c58-9aa7-3b915b006464 | -6.15449 | -51.73608 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fae13fde-f488-3d1f-96b4-4d87e3d5b3aa | -2.39987 | -57.23088 | 2026-10-08 12:19:00 | TERRA_M-T | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1b4fb1ac-164a-3021-a44a-051270cec8ed | -3.57728 | -54.67471 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| ded9efa9-38fd-365c-a419-e09f173bd180 | -1.28545 | -55.41785 | 2026-10-08 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 648137d4-9cd7-3d9f-a5e7-8e60a563f8dc | -1.42728 | -55.71672 | 2026-10-08 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b76ea5e5-b412-30ab-ba26-c2f8de6ae11d | -2.84401 | -57.47802 | 2026-10-08 12:19:00 | TERRA_M-T | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 1d2f2b1e-e1a8-3671-ba82-69d0d550a4ee | -4.34276 | -55.13095 | 2026-10-08 12:19:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cb3194da-d6e5-31f6-b665-a6a6d4f86b49 | -1.60813 | -55.1602 | 2026-10-08 12:19:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c2031880-0bf4-3299-8b97-add8d1cecc40 | -2.50441 | -56.18149 | 2026-10-08 12:19:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b8845e1e-bdd3-33ad-ab68-095d9013ad04 | -3.43933 | -56.93294 | 2026-10-08 12:19:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f27031b9-aeba-3aa3-a829-7533bff61aed | -10.43669 | -47.29748 | 2026-10-08 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9cb85860-247f-37dc-874c-d215a388bc2b | -9.57121 | -59.26877 | 2026-10-08 12:19:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18c79987-f908-34de-a3d3-66b14f8f9399 | -6.13017 | -53.05735 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bd459111-3d0f-3d75-b6af-2b66ef6a74c9 | -6.77907 | -50.66061 | 2026-10-08 12:19:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e892827b-5d04-387a-9222-4677f0d74aab | -3.26444 | -54.01722 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| f2895406-01b6-3a86-9a5a-6890962c7d45 | -6.24066 | -52.85351 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |


[Clique aqui para ver as próximas entradas](README207.md)
