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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 672522a3-a519-3c4f-a364-1ee67b5e8035 | -8.8841 | -60.7699 | 2025-08-27 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 241.1 |
| 3f8bf3b0-6705-3e7d-be00-833451004478 | -6.5769 | -47.3881 | 2025-08-27 00:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 59a9cef7-c6d9-394f-86fe-a5028c19ed9e | -6.8228 | -58.9753 | 2025-08-27 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| cda9396b-313e-3e4f-b985-22a18b7f96c7 | -9.0816 | -49.6068 | 2025-08-27 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| d41322fc-3baf-3495-a971-74fcff1c44ef | -9.4061 | -60.5518 | 2025-08-27 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 6278e3b1-b9e1-38e2-b21b-faa00559aedc | -21.5984 | -47.48 | 2025-08-27 00:30:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 605ab3e8-27f5-3635-a608-0a3effc7c5f7 | -10.0978 | -62.8895 | 2025-08-27 00:30:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 01c70782-3394-3894-b632-95af022c17f1 | -9.1715 | -59.5599 | 2025-08-27 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| cdfcc1f6-0b3b-38cf-b9d2-0f5ca7e223c9 | -9.425 | -60.5124 | 2025-08-27 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 1fe30ec8-303f-3538-9d98-9c065a7bb948 | -9.1007 | -49.5835 | 2025-08-27 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 187.1 |
| f9f017dc-59fc-3cd7-be59-6d2cfb763007 | -8.9026 | -60.769 | 2025-08-27 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 7ba9505a-1efd-3ce2-b299-4c1d33005571 | -9.1715 | -59.5599 | 2025-08-27 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a473e27b-4be4-3767-8b81-908daa1b5835 | -9.1007 | -49.5835 | 2025-08-27 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 235.3 |
| b5603b17-e9da-3352-b3c4-3ee6391ff90f | -10.0978 | -62.8895 | 2025-08-27 00:40:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a3766e7d-d713-3565-9962-c09893ab065e | -9.1527 | -59.5803 | 2025-08-27 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 3a9bc8ca-ddc6-3ec2-bd81-a8eac6422d85 | -10.2742 | -64.5096 | 2025-08-27 00:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f7ef8dd6-7aaa-3d5d-892c-cab982f255c1 | -8.9028 | -60.7498 | 2025-08-27 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3b71ba56-286e-3c43-9c51-92880e2f19bd | -21.1064 | -48.8566 | 2025-08-27 00:40:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| d6097de3-89d2-36c7-b645-a0f200cd99dd | -10.2743 | -64.4907 | 2025-08-27 00:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 58f5fea7-d40d-34b0-9b3a-9f8c0485d160 | -15.6171 | -52.7207 | 2025-08-27 00:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 75c8e0d8-b5b9-3a2c-a1ca-b026d7147fba | -9.0771 | -66.0695 | 2025-08-27 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| bb36ea19-b80d-3677-92af-37c9f2710734 | -5.118 | -43.2198 | 2025-08-27 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c6725993-0117-37f2-9f16-9a4ceb44b472 | -9.8101 | -64.2642 | 2025-08-27 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 75c3f622-5333-3f7a-b27a-4f98e463c61f | -9.7916 | -64.2461 | 2025-08-27 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5ad82210-1071-3bb8-8471-b75a44b6bba6 | -6.8413 | -58.9552 | 2025-08-27 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 83867e1c-2299-32fd-8a55-316e2c079800 | -8.8842 | -60.7507 | 2025-08-27 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 98acbf44-3205-36aa-b3e6-0e8a0c56c688 | -13.1837 | -45.2865 | 2025-08-27 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 209.8 |
| 198108a4-1f8a-3341-957a-859130cab742 | -13.1842 | -45.2633 | 2025-08-27 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d01baf25-ca20-3c9f-8d5b-885e9538eb89 | -5.5397 | -44.2552 | 2025-08-27 00:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 53be51c5-1370-3b24-b6ce-34a3222565fd | -13.1644 | -45.2897 | 2025-08-27 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| b6858bda-d042-3b34-907f-b125ef243466 | -9.1529 | -59.5609 | 2025-08-27 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| aecc3d17-c49a-3a8b-a82d-f437474721fa | -21.1071 | -48.8334 | 2025-08-27 00:40:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| ba095e6b-5e81-3ab8-a54e-cebcfd28a83a | -8.8841 | -60.7699 | 2025-08-27 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 211.5 |
| 895122a9-1e92-3af4-9e1d-a6c8cc6d95c3 | -9.8102 | -64.2454 | 2025-08-27 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0225b4e2-f61c-3256-b512-201e21c5bd6b | -9.0821 | -49.5638 | 2025-08-27 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| de045919-0db8-3164-a9e5-e399065061a7 | -9.5811 | -55.3713 | 2025-08-27 00:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 890cdb79-a1dd-3b21-a791-664dafbbd7e7 | -10.0977 | -62.9085 | 2025-08-27 00:40:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 458b4b5c-9572-3b27-834e-595eefa3991d | -6.8412 | -58.9746 | 2025-08-27 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 8bc7eea7-c42e-3d38-b35d-4546314f602d | -9.1009 | -49.5621 | 2025-08-27 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 144.6 |
| c81b07a9-24f5-3128-8309-b4f1486cdbd8 | -9.0819 | -49.5853 | 2025-08-27 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| fc8da0ae-6821-3602-8579-6b17216e6701 | -9.7915 | -64.265 | 2025-08-27 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 7b222bba-8107-39ed-ada7-fe5f3dd801b5 | -5.1181 | -43.1964 | 2025-08-27 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| babcf7e5-52f3-3edd-90d3-02631ff7b90d | -5.5584 | -44.2539 | 2025-08-27 00:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 07814d43-5d12-36a5-a677-6ae6f5cf8e88 | -6.8228 | -58.9753 | 2025-08-27 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 476d305d-2743-33e4-87da-8e7d8ca86044 | -5.118 | -43.2198 | 2025-08-27 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 02d44229-182f-3b7d-b46d-fe6130940a6b | -6.8412 | -58.9746 | 2025-08-27 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 151c0b8c-f2b5-3326-83e7-13ff356be3ae | -8.9026 | -60.769 | 2025-08-27 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 76998c37-ef35-3c01-892d-d592b3d2a413 | -19.5767 | -47.5367 | 2025-08-27 00:50:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e7f0a372-b589-3c65-b08c-5e319cb7c565 | -10.2742 | -64.5096 | 2025-08-27 00:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 34.8 |
| c185334a-a2fb-381d-9663-3fc91691dc50 | -9.1009 | -49.5621 | 2025-08-27 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| e68ea954-64fb-3256-999e-ad7bb1bcb93a | -9.7916 | -64.2461 | 2025-08-27 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2d99169d-5efb-3707-a3e1-a3176870a8ef | -8.8842 | -60.7507 | 2025-08-27 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 7516ad77-1002-3350-b3a5-a90a462fe508 | -9.1715 | -59.5599 | 2025-08-27 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| c381163b-9ee5-3119-862c-d6c6367984a1 | -8.8841 | -60.7699 | 2025-08-27 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 217.9 |
| e9663582-8248-39d6-9f62-283bebbc9938 | -13.1648 | -45.2665 | 2025-08-27 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| a50a48ce-3b56-39a4-bddb-0fdd98e5fc54 | -9.1007 | -49.5835 | 2025-08-27 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 202.6 |
| 4ea66386-2855-36e1-98fd-bf8dd5a702dd | -9.0821 | -49.5638 | 2025-08-27 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| f70addee-762e-337b-bc37-517bdae52826 | -9.1717 | -59.5405 | 2025-08-27 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0b74f0c7-191c-3ecf-9114-4159bcb1f9f5 | -6.8229 | -58.956 | 2025-08-27 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b55eb3fa-d603-3c15-a312-986f06caacda | -6.8413 | -58.9552 | 2025-08-27 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| e02597a2-db0a-3f7d-906f-a379caa1f33f | -9.0586 | -66.07 | 2025-08-27 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| a309fdfc-b8bb-303d-aac6-3dc58ccb27e1 | -8.9028 | -60.7498 | 2025-08-27 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 5ac8eba2-4881-32c7-9009-71228b3381bf | -12.9068 | -44.658 | 2025-08-27 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 43e5e7c9-fef6-3d1f-889d-6605ea169a76 | -9.1529 | -59.5609 | 2025-08-27 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 1991c50b-26b2-3335-97c1-010e150226cb | -9.7915 | -64.265 | 2025-08-27 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8a7e39da-9998-3779-ac6b-4596a3427bd1 | -6.62 | -53.3373 | 2025-08-27 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 258aba7e-8b72-367a-8082-8e24eb800f93 | -9.8101 | -64.2642 | 2025-08-27 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 989f0742-3346-30cb-81b8-220a69665b47 | -13.1837 | -45.2865 | 2025-08-27 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 8fb4845b-c27c-3490-a969-0682b0bfcbca | -10.4198 | -57.7034 | 2025-08-27 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c9ed3d1f-3ade-33b4-8863-32d5c224863c | -6.8228 | -58.9753 | 2025-08-27 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 2020429c-0acf-378f-9f70-b92a52271dd0 | -9.0819 | -49.5853 | 2025-08-27 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| b730f0e7-29a8-3d6d-8fd1-144c650e0bc3 | -9.8102 | -64.2454 | 2025-08-27 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 226bf133-4d93-3f7d-9c69-bdcb658e1e94 | -5.1181 | -43.1964 | 2025-08-27 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b571f6f9-7928-3e95-ba1f-4225f9201a2e | -13.1644 | -45.2897 | 2025-08-27 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 0e6b3814-34a2-3212-bd99-181421008d62 | -6.8412 | -58.9746 | 2025-08-27 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 5de35cb6-e623-365f-a30a-c74fb46141dc | -13.1644 | -45.2897 | 2025-08-27 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| cabbd8cf-6f29-3b38-bbec-c5ed5082795c | -9.0771 | -66.0695 | 2025-08-27 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 17c55dd2-2ede-3e9c-8a72-b6a8a9addcd3 | -5.1181 | -43.1964 | 2025-08-27 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ba06b085-3f22-36ff-bff5-625cfa3fe3f6 | -13.1837 | -45.2865 | 2025-08-27 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 157b06e9-c438-357b-8d6b-6bd56d1e72ba | -6.8228 | -58.9753 | 2025-08-27 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 5a97cec6-c669-3e0f-b81d-691052563d9e | -10.2742 | -64.5096 | 2025-08-27 01:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 33.2 |
| cba69cda-342c-3142-bfdc-8e0d75aa355d | -12.9068 | -44.658 | 2025-08-27 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4aa1b449-4d90-381b-ad90-6e88d7b255c1 | -6.8413 | -58.9552 | 2025-08-27 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7d71e6e6-9ae2-3f22-9c6b-444ebe56b6ec | -9.7916 | -64.2461 | 2025-08-27 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 35ec9658-0342-3d4a-af21-896f8530131e | -9.0819 | -49.5853 | 2025-08-27 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b1df9155-6771-3acd-853e-746bb3dd5bb4 | -8.9026 | -60.769 | 2025-08-27 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| c3098e1d-cf77-3647-abf2-976cd4614d84 | -7.2914 | -47.0014 | 2025-08-27 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| f654e50b-2881-32ae-b672-2789344e6549 | -9.7915 | -64.265 | 2025-08-27 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ef320b8b-903c-321f-a5f2-234e81dca30a | -8.8841 | -60.7699 | 2025-08-27 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 264.7 |
| 4a2cfac2-e3ce-3ba3-bda6-76ed912a31f3 | -21.5776 | -47.4852 | 2025-08-27 01:00:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3c313299-ae46-3a22-85e7-8cc3fe3af169 | -9.0821 | -49.5638 | 2025-08-27 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| bb1de7d1-25ef-3dd7-b08c-0a15e8d1ecd1 | -5.118 | -43.2198 | 2025-08-27 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 52a9aded-e218-313d-afc3-7f915b092016 | -17.4781 | -40.0753 | 2025-08-27 01:00:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| f5437eb1-b367-3862-a6d7-0cbcba4cc35d | -10.2743 | -64.4907 | 2025-08-27 01:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 719bdab8-4099-3b2d-803f-b81b50a8830e | -9.8102 | -64.2454 | 2025-08-27 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 11a54725-2040-310a-86e9-99c94b549d4c | -9.1009 | -49.5621 | 2025-08-27 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 4ea085a5-2e58-3ce0-ab16-872ce581b213 | -16.5021 | -49.4805 | 2025-08-27 01:00:00 | GOES-19 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b5619971-e9ac-35dd-b5b4-62a9405a1453 | -17.4983 | -40.0698 | 2025-08-27 01:00:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.2 |
| 2ae1b4c1-58f0-3dfd-aacf-c004c9e1d687 | -19.5767 | -47.5367 | 2025-08-27 01:00:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 27da5216-e105-3439-bca9-c8319ec8d5de | -8.8842 | -60.7507 | 2025-08-27 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 163.7 |


[Clique aqui para ver as próximas entradas](README8.md)
