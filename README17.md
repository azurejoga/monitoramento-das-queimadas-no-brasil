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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb392a41-bf97-34aa-929d-a97d6f592c6c | -5.45324 | -42.57769 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| efeb1398-9a2c-375f-b756-9f52a87464e5 | -6.99344 | -43.22907 | 2025-09-02 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a342a015-6207-3e45-a7eb-3c55f9d1f684 | -6.22803 | -43.39536 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83a79542-29f5-3738-92c1-5f7fe47da800 | -7.41812 | -44.80819 | 2025-09-02 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c812793-ddef-308c-a1bb-f1a7e988cb34 | -7.06602 | -44.34285 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79e87538-5a2c-3128-950d-96e44c02b3fa | -6.25096 | -42.61982 | 2025-09-02 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 510bab7d-9c07-3c39-8de6-1d90bdb903b5 | -6.47979 | -43.57046 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| acaf16d6-be23-35b3-b264-32c858df47be | -5.69437 | -45.95087 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4954dfb1-9f05-37eb-ba28-c7ccdc64003f | -5.69377 | -45.95434 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d026c271-b463-3e24-9ae4-1f446bedd937 | -6.13165 | -46.32301 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b3c26d2-a8ac-3fa8-a9ee-ffea5c216b37 | -6.87089 | -45.84703 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| c344cefd-c131-3391-9fa6-e475261f2eb2 | -6.86807 | -45.55873 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8cbaef3-5151-39da-bc42-07c9b5dc363a | -6.31633 | -43.51227 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4bb61e99-50df-3d09-9aa5-4cb05148b585 | -6.16956 | -44.11534 | 2025-09-02 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02c28ffa-89eb-3a81-9352-279761411d17 | -7.41694 | -44.80726 | 2025-09-02 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6919f39b-955c-3484-a915-b54eaa80c1a5 | -5.70042 | -45.95117 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54d5aa78-ec4f-3315-ba23-500e60f41bfe | -6.33759 | -42.56217 | 2025-09-02 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1048d18c-6323-3214-8538-32d3b98a9da4 | -6.97845 | -44.31008 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40da8fe6-fabf-3f95-a176-be59f6a54aca | -6.72278 | -42.25526 | 2025-09-02 03:49:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 093874db-e3ec-3e4d-8174-3cdaa21b39c8 | -3.22921 | -47.13398 | 2025-09-02 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8b9f1636-482a-39d7-b410-8a7607391813 | -6.88681 | -45.84983 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35a0e32c-1145-351d-b57e-3c23e971edcd | -6.26667 | -43.52743 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a33cd104-bde4-36d6-90f3-b60a3e2657ae | -6.18097 | -44.19181 | 2025-09-02 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a32fc5b9-070d-32e8-995e-905e55621ba5 | -3.78837 | -47.56827 | 2025-09-02 03:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcdd9c89-b69d-39e5-87dc-3b6a0ad6043e | -7.61332 | -44.03787 | 2025-09-02 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c09d421b-7ea8-3901-ae42-705a0409366d | -6.16869 | -44.12034 | 2025-09-02 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4bc5c6d-4785-3749-a351-e5e1b2e32765 | -5.68592 | -45.90253 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1237d75-49a8-3546-8885-2a3efd6e6f10 | -11.6647 | -57.3533 | 2025-09-02 03:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3e1dbf5b-427b-36df-9549-6d06f29e6ac4 | -6.8726 | -45.8329 | 2025-09-02 03:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 9ccee91b-9255-384c-8004-a678161e9e4b | -3.2305 | -47.135 | 2025-09-02 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 35d748ab-d60c-328c-b2f3-908725e0a5d5 | -7.5476 | -61.3437 | 2025-09-02 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b4a7e66c-e099-3c70-8528-f9108cea8ca9 | -6.7909 | -52.8165 | 2025-09-02 03:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e12f6ce8-8cf5-346b-837b-f8593b9ba45c | -7.5477 | -61.3247 | 2025-09-02 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d8aaafbb-ea8f-3be6-b6f8-36b76f556786 | -6.8724 | -45.8554 | 2025-09-02 03:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 214.4 |
| b35563a1-70e4-360b-8cd4-1de56a729918 | -6.8911 | -45.8538 | 2025-09-02 03:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9862bf1c-0365-394b-a6a3-c4653d040670 | -9.1207 | -61.4864 | 2025-09-02 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8b99a58f-e1cc-3f36-a097-413fc413e738 | -9.10963 | -46.04901 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bcd9ede-8c52-3288-806c-a12334e33745 | -8.46467 | -47.36687 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e3b78cf-1334-37b9-86fc-1e244ea5b076 | -13.5235 | -47.01183 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20c09355-5d75-3433-a602-beb1ab969681 | -11.66357 | -52.17614 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9f486bcc-ae1a-35b8-bf98-f03acf8f4485 | -12.86986 | -48.05322 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8799003-29e5-3a0a-84e7-e284a44bdcbb | -12.98509 | -48.10373 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9ff0a4a-6de3-38c1-98aa-430c7660f1c6 | -11.66267 | -52.21492 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 434a7938-e42d-3eba-a238-9408d596b453 | -8.19437 | -42.30156 | 2025-09-02 03:51:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9c682717-c718-3b0a-9641-b9aaf1c3709c | -8.85884 | -50.58706 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9544cd63-702e-3ddd-9c0c-526c198cbbb2 | -12.98598 | -48.09925 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 024d00af-86ee-39a5-b8cf-a7f27c4825b6 | -13.28042 | -46.89391 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0e9336a-b5b5-3d11-914e-9df44c7edb6d | -12.76146 | -44.7041 | 2025-09-02 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d404965e-82a6-3292-bfee-660cf4a536a3 | -9.74071 | -48.97101 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b6082f1-2fd5-30b5-805e-2cf671ac7d78 | -12.86485 | -48.0496 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2abe6164-cee5-3eef-a550-0a6812035a63 | -7.5525 | -45.72913 | 2025-09-02 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f34853ab-8eae-3586-94a6-997801ab14ea | -12.58288 | -44.79955 | 2025-09-02 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9e91262-1076-30f4-8b85-250a33d1b773 | -8.81787 | -47.48616 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fafc433-511f-3aa7-958f-54d73cca0b3c | -13.69896 | -46.88241 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 316e8927-6610-374a-b268-1cfedbf9de32 | -12.79893 | -48.07185 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d22e6ee-c223-33ea-8e11-2440586871b5 | -9.84068 | -48.61854 | 2025-09-02 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c2462c5-19e4-32ef-b323-38a6d5a1a8eb | -7.63287 | -46.55164 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1703168-30c5-3493-a35d-9f9362c3df5a | -12.32735 | -45.71547 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fa2271b-1a63-3017-8b84-8b4db67f2678 | -13.30724 | -46.83528 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f2d233d-242a-37a2-a0f7-332d02e33176 | -11.93072 | -50.61397 | 2025-09-02 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7923f90e-c1b6-3f5e-a0a0-b5628142476e | -11.06011 | -45.39708 | 2025-09-02 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 79602332-324c-3cb1-a1ef-d346af259719 | -10.76105 | -49.58243 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93331425-f60e-38fb-9a79-77ff2505d46f | -11.75773 | -47.82778 | 2025-09-02 03:51:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14626cf9-7d62-3371-b5af-d2841e9fc276 | -7.7048 | -45.01297 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 496c529d-c077-303b-9238-ad703d4c7c10 | -13.49994 | -46.93045 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fdcbdbf-f0fb-3c47-88f2-ba30944c6a58 | -11.67228 | -52.17051 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a02089a6-239e-36d3-a009-97e578c1a217 | -13.49545 | -46.9264 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44bad069-5f85-30e6-90a3-58937396cdca | -7.99604 | -44.04608 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 602eaf72-2039-3b66-a534-efd6004af386 | -11.09914 | -44.63549 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 50abb351-e781-3fd9-9151-62285b85e630 | -8.84566 | -45.80786 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 939d9287-533b-3f0b-9502-ddec75041020 | -12.5577 | -44.78535 | 2025-09-02 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 517266bc-a252-38aa-83ca-12f43ca0101c | -11.6699 | -52.21626 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| cfba8d16-ff51-3444-b486-8fce7a9c43d2 | -10.84126 | -45.03828 | 2025-09-02 03:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bed130f-3f90-360b-aa8a-c9d80b90fdec | -11.6671 | -52.18486 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 74a96e01-3307-3105-84d2-0e0f31c790c1 | -11.66912 | -52.1851 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 89c757e1-d88b-3275-9996-c7c32d85c88a | -7.48908 | -47.88089 | 2025-09-02 03:51:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3dd5f9fe-bd0b-3a59-acbe-a65c4b8a404a | -8.86415 | -45.79286 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14380a14-99e6-39b9-8f38-1b8255825a03 | -12.57558 | -44.78873 | 2025-09-02 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2d7facb-c714-3094-ab3f-5c9c73ef54d3 | -13.54586 | -46.97822 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48f0eca3-4606-3541-9adf-ad2481392d8d | -10.74959 | -49.57438 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5a93763-323a-3c15-8b7b-266b8bc29324 | -12.97945 | -48.10321 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa4740a8-e0d7-384d-b9d6-acb069a14756 | -7.98975 | -46.45754 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b3cc7d8b-cc48-394f-bd68-6d66e8eaf334 | -9.83948 | -48.61819 | 2025-09-02 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cca9a5a0-fedf-3448-83a0-544592d77809 | -14.49485 | -45.9541 | 2025-09-02 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00767dbe-f14d-31a0-bf95-9ccfb38cf54f | -7.98744 | -46.46502 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6baedd75-e96e-3eec-9eb2-8df470b0b8f4 | -11.10677 | -44.64474 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a59f347-fffd-3df0-8125-cca63dd49715 | -12.94213 | -48.08903 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c5858ee-66b0-31cb-81e6-f515b7389bc0 | -13.68972 | -46.93074 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f59a6d3a-4092-3db8-b4cb-340c9f60025f | -11.948 | -45.77458 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d547f7c-fa4e-3189-b19e-26d01da33341 | -13.37488 | -46.93595 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13d91284-4cd4-3441-add5-163b33a8e7ab | -11.92523 | -50.619 | 2025-09-02 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b09174f6-2318-33d9-bc5d-3eb291c9f975 | -12.87991 | -48.0603 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39ff484a-c09a-395c-9d1e-28e316fd34f7 | -14.6007 | -48.03879 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e29772c-9200-3af1-a259-9fbe42d4ca8a | -14.59858 | -48.04927 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6929141-ef4d-3e34-88c8-106f533fbf8a | -14.05307 | -44.56931 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e999623-c8b8-3947-be6f-6807f53779b7 | -14.05064 | -44.59301 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79f8b0b0-d509-32b5-aaf4-8c9188ec0d29 | -12.80519 | -48.0692 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63683a5a-bb71-3082-9a69-9b2fd6a38630 | -12.76648 | -48.09059 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb831ed2-4060-30a6-ad91-1662ff803776 | -10.05592 | -48.12701 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 504eaba4-aa85-3529-be57-ead707ab3c8e | -10.39573 | -47.12676 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README18.md)
