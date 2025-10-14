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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 123b11b4-b2a2-38b0-85db-4298b63aa1c6 | 0.39141 | -51.03524 | 2025-10-14 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8da4c444-f5fd-33cb-9448-7d0e745d17e9 | -3.43088 | -50.251 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e5c6bfb1-a264-3e1b-a28c-7e85975c4409 | -5.9637 | -42.29851 | 2025-10-14 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7bae6d4e-ee4c-323a-99c1-53e20b8ec2f8 | -2.53722 | -47.79897 | 2025-10-14 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acf51a7c-95c1-366c-a092-4f439d424cfe | -4.72384 | -45.37291 | 2025-10-14 04:23:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4870734d-19d6-3c95-a708-d54ed8eb2f6f | -4.28784 | -48.58144 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a179f9f4-c3c2-3999-886e-2b2b7be65c22 | -4.91621 | -41.52885 | 2025-10-14 04:23:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f4f9739-b514-340a-a7b0-b7092c1efb76 | -4.65884 | -43.13743 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dfa0f9fb-816f-36ab-9dff-82d1f194f497 | -6.87061 | -43.85577 | 2025-10-14 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34384fa6-e1e3-3fe0-a949-70f191939704 | -2.68962 | -49.06687 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33257ec4-e363-3f9d-a80e-7ebdc48020a4 | -6.23825 | -41.55706 | 2025-10-14 04:23:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cea8647a-7416-3108-a445-7ae854ce4c41 | -3.51024 | -49.72004 | 2025-10-14 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c45dc361-f068-34d4-985a-e6d5d9d89c71 | -5.99219 | -42.86528 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9777ccf-a804-3823-a377-a0a441421506 | -6.04857 | -43.3908 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d04589eb-bc9e-3698-a516-b3afc5e42af4 | -4.8683 | -50.62241 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09d95d89-a414-38af-a273-239f883ce274 | -4.9465 | -41.71455 | 2025-10-14 04:23:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa2b64d4-c8d6-3304-bee0-8cf5cfc61bd8 | -3.13311 | -50.20627 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8eb6aedf-0694-3a04-b828-cff9972a5c54 | -5.8622 | -43.85488 | 2025-10-14 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6f3d38f-504b-3a17-8e4c-85f72338bc66 | -5.87786 | -42.87856 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 87c2a615-6c32-3408-a68b-d1324e226073 | -5.13932 | -45.45285 | 2025-10-14 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4a71cfd-54a9-3c3a-adb8-35f4f83079ba | -5.88275 | -42.87073 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dd31db4b-ccfe-3291-9db8-8cca5ff8fe81 | -5.97112 | -42.2996 | 2025-10-14 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ac5328e-c46b-3212-9a7b-89d2db90984f | -6.23437 | -41.55648 | 2025-10-14 04:23:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 21e65f92-27dd-3522-9a6c-4bdc4cbb9493 | -5.2438 | -49.29538 | 2025-10-14 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aac538af-d576-3032-aa36-0617399b3ff3 | -3.38232 | -50.28511 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a914384e-6a03-3553-b0c9-2ea4562324f6 | -4.00468 | -43.27385 | 2025-10-14 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de412ab7-a6b3-3b0d-9bc9-a39e5463c304 | -3.26195 | -50.13174 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e825193a-51bb-3d11-a389-25997ec7554f | -6.24215 | -41.5576 | 2025-10-14 04:23:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c16c51a1-b5c2-3fc4-92af-ea125d11530d | -4.53005 | -45.58979 | 2025-10-14 04:23:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bc42762-0a09-37a7-9809-e40235e7164e | -5.839 | -42.23207 | 2025-10-14 04:23:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 582691f6-8895-36d6-adc6-d0ad2ed7359d | -3.67218 | -48.31014 | 2025-10-14 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d81eee3-bef3-35a8-a9ea-e9a0b8d7f236 | -3.05548 | -40.81286 | 2025-10-14 04:23:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8dd1f064-2c39-3a60-8482-96568bc8b33a | -4.66704 | -43.13071 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 726ba9a7-4519-338a-89e7-550b1de8b6c2 | -4.29916 | -50.39896 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06cde6a6-9fc2-319d-b9d9-fc661d0cb3ea | -4.91342 | -41.54753 | 2025-10-14 04:23:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 85158fb1-568e-337b-8bed-df6f16f94500 | -6.44722 | -41.84373 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 361fe360-1859-35fe-bc3e-bc98393d50c0 | -2.43512 | -49.37515 | 2025-10-14 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49ac5f07-68a7-3de8-b496-59c5bb28c650 | -2.86402 | -49.165 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6a098aa-9270-3bef-82cd-70ac35e90c60 | -5.88635 | -42.90837 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3b0d6e4b-8ee4-306a-a11d-6ebb8b10160e | -5.48486 | -44.63688 | 2025-10-14 04:23:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a50cedb7-0d49-3a77-91e3-069b4db7848d | -6.30009 | -42.99127 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3248bb8-a158-3b02-b4fc-54ec110f836e | -3.29662 | -43.50464 | 2025-10-14 04:23:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57304069-fc88-316e-bc6c-9ab48b407a1d | -5.56989 | -48.67226 | 2025-10-14 04:23:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be267fa2-625d-3263-a94f-9a9fbcf592f3 | -6.15612 | -41.72556 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48804acb-be5a-3a48-9e3a-ef2fea29afd3 | -6.30771 | -46.93666 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18086aa1-9db8-388b-81ad-512a1a179cf6 | -6.51218 | -44.00061 | 2025-10-14 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97124eee-b39c-31db-bf37-1d4f9d05b424 | -3.73241 | -50.25775 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f709b88-fef9-335b-a374-da2e904c0a00 | -4.39954 | -50.62355 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd5c62bf-3b1a-3616-9f59-cff7413c1723 | -6.29884 | -42.99963 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca27f035-d653-37bc-b567-b6d9af841fd5 | -5.87988 | -42.87795 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2deca73f-b8ea-3013-acba-e00fccf53841 | -5.57155 | -42.98409 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 018260a9-b2f1-3a3b-8ba3-328547a98dc6 | -5.77608 | -46.15382 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c3082fb-7dd8-3608-b3d7-e5d3ea5ca26a | 0.39706 | -51.03294 | 2025-10-14 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52cc4904-cf25-3533-9615-9306417167f6 | -6.15531 | -41.77143 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 61c30666-8f93-330b-a234-70340ef414b3 | -5.01966 | -46.76778 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 16048d4e-79a9-3f9e-b8f1-f82f7dc0fd3f | -4.4314 | -38.95952 | 2025-10-14 04:23:00 | NOAA-20 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f81af6e3-00e2-3fb0-8cd9-25265d1022d2 | -6.53685 | -43.55709 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2d03fde-e167-39ac-80b3-bc908de1f7ff | -4.28492 | -48.57679 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bd53db5-779b-3f8c-9faa-fec9421e008d | -5.96543 | -42.30176 | 2025-10-14 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e5ac2b9-8ad3-34dd-accd-1d8fa2388344 | -3.069 | -49.21641 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 251c7a0d-a773-3597-a119-5d65cf7dd58e | -3.7486 | -41.67705 | 2025-10-14 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fec54da0-80ff-343a-8109-df96dfce2dc5 | -5.40921 | -46.36885 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60d1cc77-e1ca-393b-b121-b5b1d61eaacd | -4.8244 | -43.21007 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db0378ab-b8a6-385c-9abd-cfaab15dffca | -2.9853 | -50.29643 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6013be54-f469-39d2-9ea4-8b312ec086e0 | -5.10097 | -43.20168 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d065b92-29b5-3230-b6db-0ff7ab649e5d | -4.84104 | -45.21078 | 2025-10-14 04:23:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60350d6f-ff8f-3c03-9c6d-4136fd50a0f3 | -4.67114 | -43.12734 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25005739-5c1c-3056-b377-8f7b58af71c3 | -5.64925 | -43.60616 | 2025-10-14 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 538fc97b-431b-378e-bc1e-daa4be2f1f12 | -5.62778 | -42.68593 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 43148519-8950-3c77-bc6c-60bd1fe4d8a8 | -2.83541 | -48.83444 | 2025-10-14 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57aac77a-a054-3cfc-8c0b-7e64857e56da | -5.49278 | -45.40915 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 400ed118-45e9-3426-8eef-a683db9ab5fd | -2.22195 | -51.78122 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c8bd4d8-c006-327e-b17a-47f25894964a | -3.70309 | -43.21033 | 2025-10-14 04:23:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dfd855b-41c5-3991-b58c-1af15f0c2579 | -6.33475 | -44.01728 | 2025-10-14 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01bb4a92-061d-3a7e-9887-4b6657366f67 | -3.16151 | -49.17404 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca4edc1d-e409-38bc-a9c1-b55020842fb1 | -4.84661 | -43.20549 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9586d3d2-fa5e-332d-b625-79c9fe9e9c1b | -6.53713 | -41.62358 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b022108-e4cb-3dbb-8c4a-9a71454443ee | -4.84144 | -42.76963 | 2025-10-14 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cd8165f1-f6d2-3d69-a791-1ec30c904cee | -5.87722 | -42.88266 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6fc01681-a3ae-38e6-8631-9b5db51b5135 | -4.825 | -43.2062 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5252b859-4174-3547-8cb3-881d5bdb0c24 | -3.04345 | -40.11631 | 2025-10-14 04:23:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 4f2852eb-bf43-3340-a41f-3ae1956d6062 | -5.96236 | -42.29683 | 2025-10-14 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 679bacc4-3aa0-3abb-a729-f6d308d3b237 | -3.73537 | -50.25483 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb8af086-bcc6-38a8-924b-de89cfd2fb7d | -5.94126 | -43.73125 | 2025-10-14 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed2b3547-f520-383a-81e8-bb9c02c7e999 | -5.98733 | -42.87288 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3880fcc0-0bf4-3359-a2aa-c79e13b7205d | -5.9186 | -42.81617 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bcff6746-8094-3a0b-9224-4ce50eb7b7f8 | -2.99047 | -50.29011 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9639c25-0846-35af-a0ef-58a7297ad365 | -5.88512 | -42.91654 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1bdac84f-35ed-31c5-870a-051310d87418 | -5.65213 | -43.6105 | 2025-10-14 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ecef5fa9-3b08-3964-9f4d-738436b36adf | -3.87891 | -50.97561 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2efca51b-8325-3b20-a722-ace075fcd0f5 | -5.63113 | -50.03135 | 2025-10-14 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2db745d2-a144-3c7c-8ec2-4e4c153297ab | -2.8727 | -45.43407 | 2025-10-14 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d72a676f-48f9-3bca-ad6a-060f82640009 | -5.25097 | -45.23932 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 498bdd88-9125-305b-a417-04531b15cf52 | -7.0813 | -41.94634 | 2025-10-14 04:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9247e333-da87-3544-b9b5-8ae1777b40fd | -6.29586 | -42.995 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 193b57e4-ee48-3012-8f22-35574e24910f | -6.53919 | -43.56539 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f9533ff-324d-3910-b26e-12755fbbe35a | -2.44742 | -48.88983 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e54b9ae-ef7a-3f8a-9d96-6b861e320210 | -4.28427 | -48.58086 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55f1edb0-05c8-38b9-a727-e047f25e9393 | -3.43543 | -50.24822 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 80b88226-cd45-3eeb-bd47-2093d698b3f6 | -3.1435 | -50.44894 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
