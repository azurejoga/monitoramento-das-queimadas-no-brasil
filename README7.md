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
| 91920856-c999-3aef-842c-9fac356585ff | -11.69467 | -55.4561 | 2025-05-26 04:49:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6bcfcb1b-ab6d-3dc6-b2ff-c614e15388af | -11.2956 | -54.01659 | 2025-05-26 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0d519ea-4ed7-3c93-b445-937cbc334ea8 | -11.14241 | -53.92986 | 2025-05-26 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32ac081f-4f69-37cb-9e25-06b36b19ab63 | -10.45535 | -47.94242 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac0a147c-b4f7-3b35-977e-c932be53699e | -9.22683 | -50.62661 | 2025-05-26 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 74e89837-b961-3ca9-8e04-2e7163f842d7 | -10.64992 | -46.96345 | 2025-05-26 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 909ed4a7-43ab-3930-b41c-ea439deecae7 | -10.70046 | -48.59217 | 2025-05-26 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d32a71d-d6a9-33f5-aefc-044257c8c588 | -10.45088 | -47.94656 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e76396b9-6e83-373b-bb98-a8962ef873bd | -9.7309 | -48.31825 | 2025-05-26 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b5ef7ed-3d79-3e16-a3c4-b04868a7b939 | -11.99478 | -52.47255 | 2025-05-26 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 066ad26c-145b-371a-ad8c-b68309b28775 | -14.88263 | -47.85566 | 2025-05-26 04:49:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83f53c92-7b5b-3f8a-a3a6-dbaf5a796c79 | -9.98111 | -52.13634 | 2025-05-26 04:49:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e99b8320-d37b-3987-a0ac-9b9b3d46b69a | -13.65355 | -45.55967 | 2025-05-26 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce7fdf73-b57c-392b-9605-f1442d1f4fa9 | -10.64129 | -46.96592 | 2025-05-26 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6eff5a17-f1f0-3b1f-8b69-77065a061441 | -10.45916 | -47.943 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a5e0817b-6b31-3a01-920d-4e3bb478af24 | -13.78304 | -54.31685 | 2025-05-26 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c8e2a0e3-624e-34ab-accb-4254246729b9 | -10.49575 | -42.42112 | 2025-05-26 04:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6dc54f1b-29ee-343e-a3da-7c68f284f0d8 | -11.29218 | -54.01601 | 2025-05-26 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80142ca2-db15-3a09-bfc1-e0cf98cef303 | -10.45599 | -47.94527 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa00c058-9de2-3e4d-ade7-f48ef34c0d13 | -11.75589 | -54.23085 | 2025-05-26 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 963400dd-2065-35a5-862a-5e86e653c9b2 | -11.56857 | -47.92705 | 2025-05-26 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 898f7838-c952-33c6-a317-2accbf6b1817 | -11.36489 | -55.1254 | 2025-05-26 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cfad524-8df9-376b-94b5-412867fd873c | -12.30426 | -47.48158 | 2025-05-26 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aedb04d4-8705-3c3a-a7b2-1c1916ed6f37 | -13.3553 | -48.0231 | 2025-05-26 04:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa442ab2-1477-33dc-8b06-dae1ca73df45 | -10.94949 | -48.14796 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97dec42d-fcb5-3aad-9bcd-dba5f19597c3 | -10.15209 | -51.6098 | 2025-05-26 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9003da6-bc2c-3cdd-a293-1c155e1b3219 | -10.94501 | -48.15206 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f69b43b7-ae91-374f-b1bd-89fb725755b1 | -9.97667 | -52.14282 | 2025-05-26 04:49:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39757469-96d0-33e6-9951-ed89c0b1e70f | -13.53466 | -46.72974 | 2025-05-26 04:49:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f40c591d-9fcd-36d4-ae82-c4c5c8be2870 | -10.65398 | -46.964 | 2025-05-26 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f79624b1-cb4e-3c1e-9b43-a8f04576b690 | -9.9739 | -52.13878 | 2025-05-26 04:49:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dae0a0c-13c1-30cb-ac6d-ceafdd1cb77b | -11.99146 | -52.47201 | 2025-05-26 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72c011b3-9dcd-31bf-8206-82025110a7cc | -10.45218 | -47.94469 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb1c51a6-5933-3141-9a8e-864995fce77f | -13.78644 | -54.31742 | 2025-05-26 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 525f309b-b57f-3bdf-bf31-0f63309964a6 | -9.38167 | -48.41669 | 2025-05-26 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edab972e-a033-3039-84b6-85af230ab24b | -11.28813 | -54.01919 | 2025-05-26 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f29d172-9e2a-3480-ad41-1070e227afa0 | -9.37434 | -48.41556 | 2025-05-26 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ea48da0-e50c-394b-bcf6-75ec9914b174 | -11.36625 | -55.11717 | 2025-05-26 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 964b34e7-0851-3f23-a10b-a20663138e45 | -11.29903 | -54.01717 | 2025-05-26 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56ada603-a769-32ae-a743-afd85dcf93b9 | -9.79624 | -48.52938 | 2025-05-26 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57daf368-4223-38b9-8234-cfa73c8c7de9 | -13.78705 | -54.31369 | 2025-05-26 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c3e8b11-ada1-3d11-a9d2-db1f28958bf9 | -10.45468 | -47.94714 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e173c467-de93-31c6-9a31-7fb35fcbe2c2 | -11.14301 | -53.92612 | 2025-05-26 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 270383db-e663-31ba-9175-13e5ed77d9b9 | -10.65286 | -44.49486 | 2025-05-26 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d329875-5d91-3b0c-b641-bf2df7cc526b | -13.3293 | -49.22054 | 2025-05-26 04:49:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba299b12-fa42-3100-9761-1b7caa80713f | -8.30616 | -55.10972 | 2025-05-26 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9f5b3e6-c81b-365b-8f5b-115f0f635cf3 | -10.45849 | -47.94772 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efc7577c-36ab-306f-b525-e1e71c4c62d9 | -11.75381 | -54.23069 | 2025-05-26 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 970a9d6c-48cb-3a53-bc04-48415b3693d2 | -10.64536 | -46.96644 | 2025-05-26 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1f7160d9-4ee5-3cba-9cbe-51a5d2c0ccb7 | -9.97334 | -52.14229 | 2025-05-26 04:49:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59f3b5f6-a1d6-3cae-8cea-741ca3be3899 | -10.4598 | -47.94585 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c1dd03f-c75e-3308-a165-39d71b6cc11b | -11.29156 | -54.01976 | 2025-05-26 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0750d327-9940-3f30-bf2b-ccdaa0ac9832 | -9.97722 | -52.13932 | 2025-05-26 04:49:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd78df82-fad1-370f-844f-31122584368e | -14.03993 | -55.12831 | 2025-05-26 04:49:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cb71f5f-7d8f-30a8-ac87-0c68e754e94a | -14.0421 | -55.13676 | 2025-05-26 04:49:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c659005b-a4e2-399a-92b3-3c7c7be45d28 | -11.36915 | -55.1219 | 2025-05-26 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9548fcc9-edf9-3ca8-9188-94cbbbd846ec | -11.55713 | -47.61462 | 2025-05-26 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1c2dd74-cf04-3e12-9e21-7d88928fa66f | -11.75246 | -54.23025 | 2025-05-26 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6896932e-8526-3abd-83ac-42b73dbfe226 | -12.95556 | -47.97095 | 2025-05-26 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 562c2d57-58bc-399c-afbd-93cf8ae5dded | -11.56107 | -47.61518 | 2025-05-26 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6796d50-a106-396b-8692-6bf484a36319 | -9.37498 | -48.41125 | 2025-05-26 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 435ae8ed-327c-330f-a712-014586435518 | -14.02404 | -55.13758 | 2025-05-26 04:49:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8ac3853-b67a-3a70-9969-4c95b847383e | -11.86911 | -52.25677 | 2025-05-26 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dfc5b00-8c41-366b-94c0-b77464206fd5 | -10.49528 | -42.42479 | 2025-05-26 04:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 05bdf364-ba4b-3a7a-b67f-32faf1f9ade4 | -12.87401 | -55.05981 | 2025-05-26 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec64dada-08bc-30b1-9844-74bf46c461ec | -10.69678 | -48.59162 | 2025-05-26 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7785850c-6071-3bee-8083-0173db092996 | -11.29771 | -53.98233 | 2025-05-26 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 245e0368-c58e-3e71-a144-77fb97006e0e | -8.0312 | -43.1964 | 2025-05-26 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| bdfbc04e-57af-3204-a4a1-a597ee6fbfcd | -20.60295 | -47.55287 | 2025-05-26 04:51:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2651386c-7bb7-35f8-9eae-478190a7b0fb | -20.28059 | -50.74846 | 2025-05-26 04:51:00 | NPP-375D | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b5daebe0-c11d-3302-92ba-aed6200c4d3d | -20.4767 | -53.67636 | 2025-05-26 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86621624-e008-38e9-ad1f-d3c364177548 | -16.61367 | -52.13028 | 2025-05-26 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c9a7664-4801-3a31-a73d-b2cd1251b432 | -14.68315 | -52.68451 | 2025-05-26 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 626175f7-3ec6-32b4-a1a3-93a6ee2243d7 | -16.61423 | -52.12659 | 2025-05-26 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d32b179-acdd-3bb2-b717-75812329bd37 | -19.87523 | -54.36285 | 2025-05-26 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d769bdc-064b-3db8-bb44-b3127902faba | -19.02096 | -57.62313 | 2025-05-26 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9674232d-3141-3775-b57c-539f3f6edd59 | -20.61129 | -48.86535 | 2025-05-26 04:51:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 73488ae4-474a-303a-9afa-ed6435d5208c | -16.4567 | -51.64611 | 2025-05-26 04:51:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b09d9d4-b84f-376a-b901-0f7bd08fd2e4 | -20.6108 | -48.86919 | 2025-05-26 04:51:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ad0a0146-ad8c-3184-bb33-13a08f2d6f3b | -22.23018 | -49.97559 | 2025-05-26 04:51:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c2e99882-2a93-3bcc-b581-da602bb56bb9 | -21.27567 | -48.61815 | 2025-05-26 04:51:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7a4bc1ae-600d-38a8-b97d-5ce3500b29bc | -21.27194 | -48.61354 | 2025-05-26 04:51:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 47eafe58-dad9-3962-b6bc-1653d8302c1d | -20.94028 | -56.59703 | 2025-05-26 04:51:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b24289cd-3832-3964-be1b-db5ecf46befa | -20.60669 | -48.86859 | 2025-05-26 04:51:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2bbebca2-707b-352b-b0b2-30bf5093573e | -19.7129 | -54.61403 | 2025-05-26 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46974dfe-7816-32c0-8056-dddac6562ca6 | -17.54047 | -46.90165 | 2025-05-26 04:51:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f59eea96-f301-3c2a-acf9-5e65fcdc7c1a | -16.68072 | -43.88372 | 2025-05-26 04:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3250ccd3-73ec-3e46-ba6d-61b5a5c655c0 | -21.27617 | -48.61411 | 2025-05-26 04:51:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7f5c4c8f-fcd6-3be4-aac2-9e652ff8adfd | -20.60717 | -48.86475 | 2025-05-26 04:51:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fb914e90-5bcd-3e0c-9944-de04bc0bbb66 | -19.87798 | -54.36712 | 2025-05-26 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 540fc589-154a-346d-a986-c8aef7709d36 | -19.87465 | -54.36653 | 2025-05-26 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 14c92cb7-f9dd-329a-9ccc-57300e45b432 | -19.6464 | -47.16668 | 2025-05-26 04:51:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f164829-e94b-349f-8859-b97091be6aad | -19.87856 | -54.36344 | 2025-05-26 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa699de1-0db9-3b2d-afbc-65b31fe5231c | -22.53829 | -48.81322 | 2025-05-26 04:51:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40d33dc1-d1f8-339e-ae7e-d449aaea39ea | -21.84929 | -50.55837 | 2025-05-26 04:51:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d772a875-9b58-3763-bc40-506c61faf751 | -20.94096 | -56.59302 | 2025-05-26 04:51:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6739858-5f74-3356-8366-a38c333bb602 | -22.89929 | -43.75223 | 2025-05-26 04:51:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c358e815-d919-3040-b576-d5eacd67a4da | -23.18953 | -47.10762 | 2025-05-26 04:53:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5e088fee-0ed3-3966-a0ff-fa12bf528084 | -22.21441 | -56.19782 | 2025-05-26 04:53:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6c1c91f-08cf-3ff6-aaf9-7a207b3baba4 | -23.33902 | -46.77538 | 2025-05-26 04:53:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
