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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac3d9351-dfb3-3d32-8295-3384c44f311e | -10.7051 | -49.4853 | 2025-06-13 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| d8980e5c-ed24-3164-ad01-0347c5400418 | -10.9167 | -56.8336 | 2025-06-13 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f2dbe2a8-39e3-3d94-8509-51c51c660d48 | -11.5647 | -54.5794 | 2025-06-13 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 79f84a98-3787-320c-88c9-64c05faef9e0 | -9.4114 | -57.5529 | 2025-06-13 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 11e59444-aabb-376a-b4a0-b10986259e51 | -7.2403 | -43.1134 | 2025-06-13 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 9f654774-40a8-341d-a176-3e2993779c92 | -10.7048 | -49.507 | 2025-06-13 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 0dbe99be-15cd-37e9-889f-dbf88b0c91dd | -7.4575 | -45.5116 | 2025-06-13 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 48eb94fd-bb9b-3854-bf0b-c56be3c0b8f3 | -9.3927 | -57.5541 | 2025-06-13 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| e09ca096-8aad-3aa4-a0c6-5478e056e270 | -13.9059 | -54.6291 | 2025-06-13 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 92def9af-94c2-3675-92be-2ff6bf18864a | -10.9355 | -56.8322 | 2025-06-13 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 933517e3-fa2b-3073-ad83-9a90324447cd | -8.8165 | -46.682 | 2025-06-13 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 5decb706-5b3d-3d32-8519-5995847274bc | -21.34682 | -48.5964 | 2025-06-13 00:56:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |
| 775e3121-9b33-3d4d-a4cd-e74b5a5f86d7 | -21.34828 | -48.6695 | 2025-06-13 00:56:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| f37729a6-7263-39d1-91ec-b0481933c240 | -21.35331 | -48.58901 | 2025-06-13 00:56:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 4e821a05-ca83-3912-aa8b-8704ffe1da5e | -13.90579 | -54.61398 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b0b4e7b1-4458-3a3c-a44e-8ce8d0aef412 | -13.0895 | -52.28849 | 2025-06-13 00:58:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 28c8ca16-1a05-34de-8e0c-7b2de56b095e | -13.89627 | -54.61522 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 23bef1d6-72a9-3289-9632-99c2de5fae1f | -8.95047 | -47.27214 | 2025-06-13 00:58:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9796580c-94cc-375c-95e8-6350d2a75775 | -10.65129 | -44.49007 | 2025-06-13 00:58:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 925fd06e-32f5-36ed-b50c-6970cd1608d7 | -11.57713 | -54.57463 | 2025-06-13 00:58:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c97e6d26-e2f8-32fc-b6f8-4681e094f37a | -14.67384 | -53.37535 | 2025-06-13 00:58:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 069641dd-5b40-3296-aff2-00fbe05989a5 | -11.79892 | -56.97155 | 2025-06-13 00:58:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7798f456-d9a5-3e79-87c1-e63e0eab2bce | -10.63678 | -49.41982 | 2025-06-13 00:58:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| efba850b-5159-37f4-a1e8-9810231068d7 | -11.56788 | -54.57587 | 2025-06-13 00:58:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 2ebc5e0e-8ffe-378d-b3f7-55097242f3ef | -11.13315 | -54.21749 | 2025-06-13 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 47377e04-f970-390a-b423-255426710490 | -12.10095 | -48.87243 | 2025-06-13 00:58:00 | TERRA_M-M | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fb4357ad-15b3-3dae-b5ea-56bf4ee845f6 | -14.03077 | -55.13083 | 2025-06-13 00:58:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 34242b35-97e9-3c84-8822-fc72fd4723ea | -11.12349 | -53.94155 | 2025-06-13 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa3bd34c-be45-370e-ba5a-eb209bbae826 | -12.70814 | -58.03777 | 2025-06-13 00:58:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 762bced7-e44a-33b7-a676-68bbe6d24c48 | -14.68288 | -53.37402 | 2025-06-13 00:58:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 067a8c46-7021-390b-86f5-3bcb37fd2103 | -13.90713 | -54.62452 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 90c5c93f-6565-348f-8bed-8954832dd471 | -13.8976 | -54.62573 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 0fa159fe-f9fa-32dd-a4b2-d604119d93d5 | -14.19915 | -57.40792 | 2025-06-13 00:58:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 0097b43d-29a5-3f9c-a486-e7fc6765bf83 | -11.56656 | -54.566 | 2025-06-13 00:58:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 4c062fb5-f5d6-369b-bf64-c6155a35fe0d | -10.36407 | -57.22681 | 2025-06-13 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8154fb93-077a-3bd8-bfdf-d6d33667de91 | -8.96512 | -47.96954 | 2025-06-13 00:58:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 02eb62d9-83ac-37c4-9650-03115191fb5c | -12.00033 | -45.13919 | 2025-06-13 00:58:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 1527edbc-8404-3e8c-a626-c76f5a186b30 | -11.12475 | -53.95083 | 2025-06-13 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4d255cc9-514f-32c8-b7a8-9bb23658e01b | -13.09832 | -52.28719 | 2025-06-13 00:58:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 00923824-553e-3baf-b04e-a5700b8ca45b | -13.04178 | -50.40649 | 2025-06-13 00:58:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9e2149a3-0049-3e21-9931-14e4b5be2051 | -14.20886 | -57.39031 | 2025-06-13 00:58:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5d291a08-eccf-3e10-a9b7-78b7eb6f00a6 | -11.92069 | -57.47987 | 2025-06-13 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 03ef650e-548a-3331-b15a-48378a86a6f0 | -11.87496 | -52.29996 | 2025-06-13 00:58:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1c6761f6-d21e-303a-9009-95b71e6f1704 | -13.97656 | -54.44888 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f917fd2c-32be-38a1-aa25-e57852b821f4 | -9.66576 | -48.77599 | 2025-06-13 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b196dabc-e3f4-30dc-83cb-0ceaa90fdee6 | -13.89507 | -54.64314 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| e01648a5-b106-3cf3-876f-4ddafa8715c8 | -14.2108 | -57.40655 | 2025-06-13 00:58:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 858c09a9-078e-3bf5-882f-5151f5ca27bd | -9.40387 | -48.43393 | 2025-06-13 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0e6dc578-a990-365c-a5a9-068bd70537c1 | -14.67257 | -53.36576 | 2025-06-13 00:58:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f04f4915-a04a-37e4-8530-74d5f4b08a8f | -9.67646 | -48.77421 | 2025-06-13 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f8bbdee1-4a6f-30c8-bbf6-4a7e5e94b44a | -13.89092 | -54.61156 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1059d87e-1e7b-37b7-9fc6-b3d1e970fe3f | -11.80174 | -56.96488 | 2025-06-13 00:58:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a631fdb5-8f69-3971-a48b-cecab2271c94 | -10.64864 | -49.43024 | 2025-06-13 00:58:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 5fa0f9cd-51ed-300e-8f0d-c07774eda14e | -13.98141 | -56.01906 | 2025-06-13 00:58:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 27c11893-d545-3a70-a14d-292252fc16b9 | -12.43556 | -54.87714 | 2025-06-13 00:58:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 03b78020-5d2a-3555-9827-64b21f66a948 | -8.8078 | -46.69061 | 2025-06-13 00:58:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 45bbd360-69e1-3d8f-ae3f-b888cdccd83f | -12.00661 | -45.13235 | 2025-06-13 00:58:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| a79b9604-c542-3fa0-99c9-a04f76a83e2a | -10.65083 | -44.48453 | 2025-06-13 00:58:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3d011247-6de9-3a81-9eb4-40959dc6b355 | -14.04059 | -55.12956 | 2025-06-13 00:58:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 97fb0ca5-432f-3cdd-9da7-b164be4d3466 | -10.60276 | -52.83302 | 2025-06-13 00:58:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a8693d9e-484f-37e4-83e9-395be24a42ca | -13.98748 | -56.01268 | 2025-06-13 00:58:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e8621766-1625-3a50-b6e4-355a9604c34b | -10.64686 | -49.41827 | 2025-06-13 00:58:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| c7aa0b05-a167-3144-8cf1-7e0b8f171929 | -12.28783 | -50.10778 | 2025-06-13 00:58:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8fe43745-4863-35ed-922f-23bbe05f8e97 | -10.86962 | -54.31157 | 2025-06-13 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a6850f22-2dc8-3996-9e19-2696805dff66 | -13.08825 | -52.2795 | 2025-06-13 00:58:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e642678f-df31-3c06-8512-ebcda93c956e | -10.63857 | -49.43176 | 2025-06-13 00:58:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 29928d74-9e49-34a0-8730-9e1362cc3a17 | -10.65693 | -49.41667 | 2025-06-13 00:58:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f18b7e3f-8fd1-3d74-85ed-dd85ef24afd0 | -10.29152 | -52.84217 | 2025-06-13 00:58:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e52b9a23-ca40-3981-90e4-996c65f2d7fe | -13.89229 | -54.62202 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 9a8a6fbb-4c28-32f3-bf95-669d423a3eb1 | -10.93438 | -56.83612 | 2025-06-13 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 0e18d15d-9540-3e11-821d-d22e3fc3046b | -9.88443 | -46.26955 | 2025-06-13 00:58:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6b6a1cf3-0408-3a15-8652-498721db982a | -14.02933 | -55.11961 | 2025-06-13 00:58:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4608852d-b565-3839-9c59-d62f52455333 | -13.97523 | -54.43848 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 95200fe4-c708-3b3e-a687-5e679db04f94 | -11.13374 | -53.94958 | 2025-06-13 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| beb5b6ff-4c0a-3091-8d63-2b16c2efff4b | -13.89895 | -54.63633 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| d149c41a-7a41-389a-91af-d876211406b3 | -8.81105 | -46.71096 | 2025-06-13 00:58:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 806991ac-e1d3-39a1-ad14-dc22d8a5effb | -10.36881 | -57.23382 | 2025-06-13 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 8724072d-c727-36a5-9f4e-d003c888afe4 | -11.13986 | -53.92375 | 2025-06-13 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1664d761-1bf6-396f-8e19-126ecde0769c | -10.85423 | -53.78485 | 2025-06-13 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4144319c-e3f5-346b-a302-7c751cde039f | -10.9238 | -56.83751 | 2025-06-13 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| a5cf223b-bd9b-399d-b7fd-aa8bcd4c7c43 | -10.85927 | -54.30336 | 2025-06-13 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9b6ed9e7-a564-3a10-a183-20f3e1b78f06 | -10.86835 | -54.30209 | 2025-06-13 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 6a1a5101-aee0-3cf1-aea2-d8d8826f59c7 | -10.70005 | -49.50038 | 2025-06-13 00:58:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| cca2ea95-3f0e-394f-91db-7812a478ee80 | -8.95666 | -47.2833 | 2025-06-13 00:58:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b48eda55-fe73-3e49-b3a8-920d1d12e5e1 | -12.13166 | -54.66497 | 2025-06-13 00:58:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 16d3b25d-5dfc-3e7e-a849-07345deef91a | -10.36585 | -57.24054 | 2025-06-13 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e3d1d2cb-7c69-3bbc-b045-10e57d6ca8ed | -10.92549 | -56.85077 | 2025-06-13 00:58:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d1cec2ec-e8c3-3895-bd81-95669ce9ad35 | -10.29805 | -57.13808 | 2025-06-13 00:58:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e041ffd4-f27d-311d-bd2e-1c99df6d8788 | -9.67438 | -48.7607 | 2025-06-13 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d4ddf6c5-45c5-3ae2-9bde-d14bdf869bbd | -14.68161 | -53.36441 | 2025-06-13 00:58:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2274ebe0-228e-387a-9a3f-2550021b9db0 | -12.26547 | -44.61263 | 2025-06-13 00:58:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| af7230e8-ba38-38d7-a36d-fc4383e733b2 | -10.5919 | -49.4633 | 2025-06-13 00:58:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 86e1c209-de61-3cfa-b288-8158a8a07f90 | -10.60152 | -52.8241 | 2025-06-13 00:58:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7cf040c8-ac22-38b0-a626-aabf51026548 | -10.70183 | -49.51207 | 2025-06-13 00:58:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cb01fc1e-1bc6-34b5-97c8-c01a0ca23864 | -10.6587 | -49.42861 | 2025-06-13 00:58:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b5c7f658-80af-3bb6-94c5-88cad1abddf4 | -12.52046 | -57.23853 | 2025-06-13 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 6aa0423e-250f-3981-8d93-7d5a088e0f29 | -11.13247 | -53.94028 | 2025-06-13 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6b344875-a1ff-3a12-af55-6b1cc5094439 | -12.47242 | -58.46796 | 2025-06-13 00:58:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 241b79e0-82f0-3272-92bb-7301fedc87f1 | -11.369 | -56.56498 | 2025-06-13 00:58:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1d62e40c-e50a-371a-8a5f-f96c075be097 | -13.90028 | -54.64689 | 2025-06-13 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |


[Clique aqui para ver as próximas entradas](README4.md)
