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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55cb5a2f-5932-3d21-8dfa-b098a8ef0616 | -5.1274 | -43.2089 | 2024-12-02 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ec5813d-1166-3621-a06b-3f9083b691da | -3.2801 | -52.0424 | 2024-12-02 00:18:00 | METOP-C | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da231e8c-e4d3-3599-84e3-8e70a3b144a6 | -2.6739 | -46.605 | 2024-12-02 00:18:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c955bf9-ddb4-37d4-8e64-09e81f5b2d39 | -1.9071 | -46.4016 | 2024-12-02 00:18:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72a16946-d210-3902-9a67-18c87e5170fc | -5.9049 | -46.251301 | 2024-12-02 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba8692be-c646-3deb-b7a4-93b88c0d9d47 | -3.2539 | -53.616501 | 2024-12-02 00:18:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fce225ca-c43c-3151-a628-88a9a0936cc4 | -5.5854 | -45.142502 | 2024-12-02 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75328537-e105-34fc-8b9b-135a063b0b17 | -2.6498 | -46.771301 | 2024-12-02 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c030dca8-2bef-3909-acc1-99111c0aff5e | -1.5571 | -46.7635 | 2024-12-02 00:18:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4038d308-b7d6-3f02-827c-aca9b5d83659 | -4.6276 | -45.459499 | 2024-12-02 00:18:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c413f10-8d9e-3a06-bccc-18cdb2241bf3 | -3.258 | -53.5895 | 2024-12-02 00:18:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 797537ec-39d2-370f-bbbb-af7fd7167559 | -2.64 | -46.773499 | 2024-12-02 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0099364-fbcd-3a4d-82d8-b13487387056 | -3.3751 | -49.8578 | 2024-12-02 00:18:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df4417fe-7beb-36e9-b120-b6c1766aafc8 | -3.402 | -50.2076 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef634efa-c48c-3a09-8442-a6e066bd3798 | -3.2442 | -53.618599 | 2024-12-02 00:18:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7975328e-fb40-37cc-b565-94af1cffa1f5 | -3.3956 | -50.2243 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 146f1b81-3072-322a-831b-f9838e89b611 | -5.3875 | -44.0364 | 2024-12-02 00:18:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb291357-de22-3f66-b7cb-75f77c082ce7 | -1.9108 | -46.417702 | 2024-12-02 00:18:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b70b0bfa-2de0-3b80-864d-8ffb56f558d2 | -2.6463 | -45.485901 | 2024-12-02 00:18:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2a14172-3348-33fb-b6ca-ab522dbf9b76 | -6.3719 | -47.3438 | 2024-12-02 00:18:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c9e0fe5-9c5b-3c5c-b073-ff812fd30f52 | -2.58 | -46.009701 | 2024-12-02 00:18:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2963d7ce-ffd0-3abb-8661-91f09baa28cd | -2.3821 | -45.954498 | 2024-12-02 00:18:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffcf6ae7-6df9-363d-aac7-9ca6a82e6cd9 | -2.8114 | -53.040901 | 2024-12-02 00:18:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6de3f57-c575-3ca8-bd75-4fc5f4baccfc | -2.5602 | -45.560299 | 2024-12-02 00:18:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f501adf0-5c3e-3e90-83a6-823edb0b5bcd | -5.9147 | -46.249199 | 2024-12-02 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be2f371e-ad92-3e31-b7a0-7b98b915d80d | -2.7736 | -45.592701 | 2024-12-02 00:18:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e7f720ea-e1ed-35fb-bcc9-848db9ce2cf0 | -2.9137 | -45.348 | 2024-12-02 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c00376cb-a2a2-3b6d-bf52-e7034e36add0 | -2.3755 | -48.601799 | 2024-12-02 00:18:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4144d5f0-008d-3b2c-b0b0-0705c839aeb8 | -3.1411 | -45.487499 | 2024-12-02 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 072688d7-3881-3622-af36-10f7d014e814 | -3.15 | -51.092201 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a217e5c-1566-3301-a874-54dc204ca53a | -2.4784 | -46.560001 | 2024-12-02 00:18:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 583a1e56-8a3d-3c3b-a541-ac3474ea43fd | -5.3891 | -44.043499 | 2024-12-02 00:18:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1559c2b-aff6-3fb7-af70-77271b103a5a | -2.0922 | -46.309799 | 2024-12-02 00:18:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75bb68aa-4d2d-3dac-b032-e74cad7ac08d | -2.5482 | -53.362499 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b164effe-3c85-3541-bcbf-de76e9ae043a | -5.9128 | -46.240398 | 2024-12-02 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2be3c435-d8d9-313c-900f-5bc41e2451c8 | -2.9535 | -45.795502 | 2024-12-02 00:18:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08a62234-ca3b-34f3-b22e-75d85cf593d8 | -2.5535 | -53.385899 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38d9f270-a111-3001-85d9-33d4747ac9d3 | -3.3623 | -49.846199 | 2024-12-02 00:18:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad4c2a01-4a89-3e8a-9671-0a412ceed737 | -2.1466 | -45.644001 | 2024-12-02 00:18:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13b43dcb-03ca-37b3-a4a8-0f4263f00765 | -3.2121 | -45.754799 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ea67d32-c878-3179-be09-ce7d6ab2e8c2 | -3.279 | -46.141399 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 75799b35-9066-319d-a122-7e61c0135409 | -5.5871 | -45.150299 | 2024-12-02 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bf6ab9e-4c66-3f27-91d8-bfc604d7e45d | -2.15 | -45.6591 | 2024-12-02 00:18:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1badde-a620-3df5-9d55-e072f00a98a1 | -5.2042 | -42.868099 | 2024-12-02 00:18:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe7a9fd0-0d93-3863-989c-e6ebae04adfb | -3.4965 | -50.310398 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce381dcb-21ae-3ebd-b570-8c4927b013ad | -2.4705 | -46.570499 | 2024-12-02 00:18:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b313d384-31a7-3e78-9821-ae01ce30fa52 | -2.9232 | -45.843102 | 2024-12-02 00:18:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce6027f-03b3-3a7c-aab3-9ca1685b10cc | -2.5675 | -45.954601 | 2024-12-02 00:18:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66151e9d-0942-305a-8ff3-670a97e54348 | -1.7965 | -45.148499 | 2024-12-02 00:18:00 | METOP-C | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffd19364-7a1c-33e8-90c5-42585c40fc94 | -5.1702 | -44.669899 | 2024-12-02 00:18:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed918ef2-81b9-30d6-8cab-e21819816032 | -5.1159 | -43.204201 | 2024-12-02 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70799906-560f-33e2-8d78-4a6232f166ad | -2.5385 | -53.364601 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa56ce8b-ae30-399c-a32d-52307c18fa21 | -2.4803 | -46.568298 | 2024-12-02 00:18:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e53d3a-6042-3571-a41f-26100df298c1 | -2.4667 | -46.553799 | 2024-12-02 00:18:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 485ced6e-44d2-33f2-a8ef-366b8a011dcc | -2.4607 | -46.572701 | 2024-12-02 00:18:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d0b60a2-5b5a-3573-8065-2363f60ffb0c | -3.1394 | -45.48 | 2024-12-02 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3573998-a9bd-3ca4-872c-122b519afded | -3.1376 | -45.472401 | 2024-12-02 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cad7eaa3-e704-3ac5-b55a-6832bd04cc1f | -2.2512 | -53.576199 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e702a9dc-f81a-3878-8ca2-eef1b8048489 | -4.5253 | -45.782299 | 2024-12-02 00:18:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6350aa21-be41-3999-8b34-b9022df27b09 | -3.4053 | -50.222198 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d261dd9-70c6-3c70-9ecc-785ee67d082d | -5.1693 | -44.8027 | 2024-12-02 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d88a7378-bebd-35f2-84e9-e5adc32d790b | -3.2941 | -52.059799 | 2024-12-02 00:18:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45d7d2bd-b8ef-3df1-962c-b2635fe6c045 | -0.9703 | -47.800301 | 2024-12-02 00:18:00 | METOP-C | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 457ce81c-77fe-3f5e-93f2-ceb6e3c13102 | -2.6446 | -45.478298 | 2024-12-02 00:18:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da7079d3-b955-3aac-ac86-ac695c67a93f | -2.9214 | -45.8353 | 2024-12-02 00:18:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 600fc2e8-a1fa-3e03-9690-85d82a188a63 | -3.1292 | -45.98 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a50031a-cf7a-35e5-8bb1-6fa4c4ce77d1 | -2.5606 | -46.559399 | 2024-12-02 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac569ff-c33f-3ee0-a36f-de1185d0079e | -3.0201 | -51.5154 | 2024-12-02 00:18:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e10dc16a-b294-303e-aea7-c53a2419fa75 | -2.1581 | -45.6493 | 2024-12-02 00:18:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb346ecf-ccad-328a-8429-127b2325a645 | -2.5693 | -45.962502 | 2024-12-02 00:18:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a65f4d8c-4c73-341f-813d-1f5845f09204 | -3.3075 | -46.403801 | 2024-12-02 00:18:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5264308a-c3cc-3ebf-ba47-fd21b7d1936b | -5.1191 | -43.217999 | 2024-12-02 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5a13493-45bf-3140-aea6-9b1b1084757f | -3.1274 | -45.972099 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cee609db-4bc0-3af6-87f2-6caa6f4dd432 | -3.6874 | -51.8139 | 2024-12-02 00:18:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e40ce21-3dcc-3613-92ee-7eb58c837933 | -2.982 | -52.484798 | 2024-12-02 00:18:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d791ee06-adc1-3c9c-ab03-647ef0c0e7e9 | -2.7967 | -53.020599 | 2024-12-02 00:18:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0399c1e-038f-31fb-9268-aa4d277e0b41 | -2.5585 | -45.552799 | 2024-12-02 00:18:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 14126e7e-7ff6-32aa-a672-4edefb13b6ba | -2.2566 | -53.600201 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fb86aff-8205-3583-96f3-708ec7563e86 | -1.8164 | -46.636299 | 2024-12-02 00:18:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91c711a8-a75b-3639-965b-3157115f1301 | -2.282 | -45.741501 | 2024-12-02 00:18:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f526719c-75eb-3b80-a26f-c07c2e015e33 | -2.4686 | -46.562199 | 2024-12-02 00:18:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 180061c6-8eab-3453-ba83-a8be045367fc | -4.106 | -39.989799 | 2024-12-02 00:18:00 | METOP-C | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b8d3a146-71a3-3af5-b578-88b1f9e00d53 | -2.8017 | -53.042999 | 2024-12-02 00:18:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2ec1f45-9920-3a46-8e6b-af1d5357d7ec | -3.2844 | -52.061901 | 2024-12-02 00:18:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a54f7ded-2851-30f6-bd55-20414fb3dea3 | -3.0852 | -53.222 | 2024-12-02 00:18:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 703623d2-e8bd-3c5f-bf26-f7192c933955 | -5.1676 | -44.7953 | 2024-12-02 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cc25126-8542-309b-bdf6-25c0532b087c | -3.4541 | -50.257599 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b1973b6-87dd-3dcc-8f88-32e08f1db1e7 | -2.0108 | -54.263901 | 2024-12-02 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 732f808f-cdb3-3e94-a005-b6a8f6fea0bf | -2.3839 | -45.962299 | 2024-12-02 00:18:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| effd7105-c8b6-3740-885a-a44a1497e7d5 | -2.5438 | -53.388 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6402f90f-c01a-3fa4-a330-6b9db3c476ea | -2.2319 | -46.380798 | 2024-12-02 00:18:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1a4959b-aa48-3f59-8c7a-2d5a70975f0d | -2.1968 | -45.593201 | 2024-12-02 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a03aa5c2-3dcf-3d75-9199-3f2331613892 | -3.131 | -45.987999 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f97ef03e-ecb2-39fe-9589-bc4007265729 | -1.7982 | -45.1558 | 2024-12-02 00:18:00 | METOP-C | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc753d7a-f24b-32e3-aa4f-29782e9d9f13 | -3.6971 | -51.811798 | 2024-12-02 00:18:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5ed53ba-ced0-3c65-87fc-96aac4710374 | -2.2608 | -53.5741 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa0309d5-4530-3912-8964-1fa4846d0217 | -5.1243 | -43.195202 | 2024-12-02 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f935bcef-c8fd-36b4-b389-dea0cdda63a3 | -3.3338 | -50.222401 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5a6d782-64e6-32e3-9b92-f7b449ab18bd | -3.2484 | -53.591499 | 2024-12-02 00:18:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f4c626f-02d0-3d46-9b6e-3943699dc65e | -3.2138 | -45.7626 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
