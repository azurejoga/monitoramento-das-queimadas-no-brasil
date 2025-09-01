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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e98a9c8-cdde-3124-8543-80dcb33b9e48 | -8.6468 | -67.2515 | 2025-09-01 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| da9e1374-9839-3b47-a817-5253cd2c7224 | -7.0965 | -63.0437 | 2025-09-01 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 3f7f9247-efd6-3a84-bb9d-65f6b1b1b503 | -6.7909 | -52.8165 | 2025-09-01 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c6a17625-d9f0-328e-b8cd-0b1176854850 | -11.3701 | -43.6104 | 2025-09-01 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 020c51ee-164b-3eab-9ffb-316c4e1c3675 | -7.6967 | -61.09 | 2025-09-01 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| e81caf28-8418-3a5e-941c-d07eeb9701f7 | -6.1665 | -43.3273 | 2025-09-01 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 81880616-e617-382f-bde7-3ee0c31a4671 | -6.8281 | -52.8143 | 2025-09-01 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 4fd00c4d-a25f-344d-9c47-21416bf2d0cf | -9.694 | -65.0958 | 2025-09-01 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 31f77fbf-54be-3167-a57d-2b366f9bd93a | -6.8095 | -52.8154 | 2025-09-01 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 0502068f-e9e5-31f0-b414-2745e49bb191 | -4.9311 | -43.1857 | 2025-09-01 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| f1aba6e1-b0ae-3868-aee9-abae8eb13dbd | -9.135 | -65.5453 | 2025-09-01 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f490e35b-4e61-36b3-bc5e-23fbafc4fa22 | -15.6058 | -48.3402 | 2025-09-01 00:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 230fc542-a107-3072-aa7d-866f5cf89ccc | -7.0757 | -44.3606 | 2025-09-01 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 75b08b29-b718-3c12-a7ff-099757d6b005 | -15.6058 | -48.3402 | 2025-09-01 00:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| dd9ebe9a-dfe7-343e-b2c1-737bd514794f | -6.7438 | -43.7898 | 2025-09-01 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 11b6f4ce-3736-3ce0-822b-46f29c61543d | -8.8454 | -64.15 | 2025-09-01 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 4ffa4aac-8863-3843-8901-ca47496856c4 | -11.026 | -47.0538 | 2025-09-01 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 746ee42d-a692-3744-b153-383529dd6307 | -11.3888 | -43.6312 | 2025-09-01 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| e6b8b11f-550b-3f6f-b7b6-640a3c8ebd16 | -7.6783 | -61.0908 | 2025-09-01 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a8036032-2bc6-3293-b7b5-bea7e222ae56 | -15.5867 | -48.321 | 2025-09-01 00:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 9beb05de-8b7c-3f79-b049-0cf0a8dcd5ae | -15.5862 | -48.3435 | 2025-09-01 00:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 63caf6b7-4906-33df-aff4-2e05aa936eb7 | -9.1522 | -65.8434 | 2025-09-01 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e6cff70b-5f16-3bec-8f5d-6bc407ea12a5 | -12.5722 | -48.2059 | 2025-09-01 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 39efb44f-fa5d-3e2e-83ff-8115b885c2e9 | -13.1837 | -45.2865 | 2025-09-01 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 78ace8dc-960a-3cc0-baa5-82008613b18d | -7.076 | -44.3376 | 2025-09-01 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 210.8 |
| a1d62923-880d-37db-bb08-c0d57d57e62a | -6.8279 | -52.8348 | 2025-09-01 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 68b2f002-3332-3394-ad08-fdfd7ce30ff8 | -9.0192 | -50.1253 | 2025-09-01 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5f7e540f-7250-319f-87a9-1e3efb87c883 | -13.1842 | -45.2633 | 2025-09-01 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 75197ace-0d68-3a92-bf25-98cc36c1dabd | -14.7618 | -46.7667 | 2025-09-01 00:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 4477c5c2-4932-34e9-aa72-fb96cdd7ab91 | -7.0946 | -44.3589 | 2025-09-01 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 9458aed2-62f7-33a5-89d0-78b8434d42b1 | -7.0757 | -44.3606 | 2025-09-01 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 1c41e069-c7f5-3e10-9e4c-7d25627e6bef | -7.0965 | -63.0437 | 2025-09-01 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| b2a8a2a7-11e2-3f51-9eba-86e10a002de1 | -15.6063 | -48.3177 | 2025-09-01 00:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| ce0122e8-4115-39fc-a44d-69d81e272a59 | -13.1644 | -45.2897 | 2025-09-01 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 3f2bee90-2cfb-3acf-9e82-70a461d63f0d | -11.3701 | -43.6104 | 2025-09-01 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| ddd09491-29f8-3d23-a9ff-be227dd3d442 | -9.135 | -65.5453 | 2025-09-01 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 9984e7cf-0cac-3a3a-b746-91d4ce9bd36c | -15.7112 | -48.9032 | 2025-09-01 00:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3fe7c190-0e19-3f72-94ed-d61a95a369d7 | -6.8466 | -52.8132 | 2025-09-01 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| aa1d30ae-3dbf-367c-9475-1d3fb4e2dd71 | -4.9124 | -43.187 | 2025-09-01 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f353c358-4981-3bb4-aeac-282d7ac780df | -7.0948 | -44.3358 | 2025-09-01 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 255.3 |
| 6b209db7-81b2-36b5-9b8f-b6c495058ac0 | -8.6468 | -67.2515 | 2025-09-01 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ab5fddb2-6c75-3785-92a0-921bb2947816 | -6.7626 | -43.7881 | 2025-09-01 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c1ec75c7-adbc-37de-a867-c6176080b4cc | -6.1665 | -43.3273 | 2025-09-01 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| c5df43d1-fca7-3cb9-befc-8c0462c7146c | -11.3696 | -43.6341 | 2025-09-01 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 5c9b6601-2440-3161-9ca5-edf8037c8a5d | -9.1337 | -65.844 | 2025-09-01 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2bd9f9b7-7ee3-3484-9439-bf381a97bc5a | -10.0434 | -48.0998 | 2025-09-01 00:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 1ef1ba70-1213-3cba-93f8-1d57ebfede0d | -6.4373 | -55.6212 | 2025-09-01 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b4da898f-b32e-3840-9000-434b93f47989 | -6.8281 | -52.8143 | 2025-09-01 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a0f6580c-dc8e-3d27-b3d8-1b88f3e12138 | -13.1648 | -45.2665 | 2025-09-01 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 3b2cecee-978f-33f7-a5d7-b894e3fff927 | -10.6128 | -44.3284 | 2025-09-01 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b8bb4489-715c-3917-ad33-76235df52216 | -9.1336 | -65.8627 | 2025-09-01 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 28cb030f-0313-341f-ae8c-01fd13918a4d | -7.6946 | -61.4712 | 2025-09-01 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 12e06e7b-1d4e-3122-98ed-6a0b338ae1fd | -10.5937 | -44.331 | 2025-09-01 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d99e7963-8fab-358e-bdc6-730315f25a16 | -6.7626 | -43.7881 | 2025-09-01 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 105f1a12-d320-34d5-ad47-64d9ce68be4d | -15.6058 | -48.3402 | 2025-09-01 00:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 95f88baa-6b27-3fce-8586-cb51f1c91b99 | -13.1644 | -45.2897 | 2025-09-01 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2540ea92-cb2e-37e5-ad16-445dbdb67dc7 | -6.8281 | -52.8143 | 2025-09-01 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 09f037a8-01d0-3e54-9bd5-251e301b4731 | -11.026 | -47.0538 | 2025-09-01 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 407.5 |
| ad775d65-3190-33e4-ac39-85ba9342e4a9 | -6.744 | -43.7666 | 2025-09-01 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 93981c23-c045-3b3c-aead-6fccd75ec204 | -11.0256 | -47.0762 | 2025-09-01 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6c041175-0230-3e0e-88fc-59db25a639c4 | -7.0948 | -44.3358 | 2025-09-01 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 5af7883b-b787-326a-b741-2257ae89030a | -6.1665 | -43.3273 | 2025-09-01 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 97ec4ee6-5347-3f53-b8aa-afa59be90146 | -9.1522 | -65.8434 | 2025-09-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5e9daec2-acd8-3512-92ea-74ef7261b65f | -6.7438 | -43.7898 | 2025-09-01 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 174.4 |
| d141801c-bac4-3d47-88e1-b753aae3ddc6 | -11.3888 | -43.6312 | 2025-09-01 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b6c4fb77-48c2-3718-a8e5-e1094bd4b82a | -6.8279 | -52.8348 | 2025-09-01 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 37b8e0e4-344a-3e6b-8c3d-c7eafaead8b6 | -9.1151 | -65.8446 | 2025-09-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| ad546cf9-d786-35f6-b149-8f0953da48a4 | -15.7112 | -48.9032 | 2025-09-01 00:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 341e2828-3158-3b58-b8c0-c2496211f3e7 | -15.5862 | -48.3435 | 2025-09-01 00:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 111.6 |
| da5cfedd-77c5-3d07-8bcb-f4d389497993 | -11.0069 | -47.0562 | 2025-09-01 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 83b02b44-2f65-3029-8319-518914b7e7bf | -14.7618 | -46.7667 | 2025-09-01 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f4210e95-3cbc-3846-8e9e-246808c68d28 | -13.1837 | -45.2865 | 2025-09-01 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b6f9afd9-f6f5-33d5-8523-f3847af1b84a | -11.3696 | -43.6341 | 2025-09-01 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 39a25037-cde2-30ee-acce-9f4e70e57f1f | -10.0434 | -48.0998 | 2025-09-01 00:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| dc8c6c4e-9979-3fcb-a10a-aa9d99818d9d | -15.6063 | -48.3177 | 2025-09-01 00:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 50a54342-07ec-340a-b0b8-901d73550188 | -6.8466 | -52.8132 | 2025-09-01 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| a4c75e8e-d8c6-3717-8057-ec515dfd814b | -7.0965 | -63.0437 | 2025-09-01 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d22b3f3c-4372-3165-bb17-1a9a19029d0b | -15.5867 | -48.321 | 2025-09-01 00:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| a765ccd7-895a-3832-ad09-0fadecf8ad34 | -10.6128 | -44.3284 | 2025-09-01 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1a7726bf-a59a-3b7a-a209-4a1e125f2cbb | -11.3701 | -43.6104 | 2025-09-01 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 1a0a9a97-ae8a-379b-9898-81c2f5b0e8ba | -7.0946 | -44.3589 | 2025-09-01 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 593244d8-6d44-34e0-8174-2d95625f4390 | -13.1842 | -45.2633 | 2025-09-01 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 68ce5828-da1c-37bf-83e2-ce81424d3a3b | -11.045 | -47.0514 | 2025-09-01 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ded377c6-dffa-3fd7-b5cf-9631b57279ad | -13.1648 | -45.2665 | 2025-09-01 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 97509449-a8da-397e-a451-6f124649a378 | -6.8095 | -52.8154 | 2025-09-01 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b3c46712-feb8-3099-be2e-70603bd59b07 | -7.0757 | -44.3606 | 2025-09-01 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 9bae4430-0454-3559-ba24-31c3fe80e1a7 | -9.1337 | -65.844 | 2025-09-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ba8df404-4b2a-306a-886a-3c74f3f5e36d | -12.5722 | -48.2059 | 2025-09-01 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 3dda5635-10b1-3871-9a81-e936bd7db8d9 | -6.4373 | -55.6212 | 2025-09-01 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 51c14026-b144-37ce-beb9-c7af86aab8cd | -8.6468 | -67.2515 | 2025-09-01 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 89eaf9f3-c6f5-3ff9-9ba4-0bcc1c9feec3 | -7.076 | -44.3376 | 2025-09-01 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 235.3 |
| dbb929dc-a363-3c0d-9a90-fc5ce548a7ab | -11.0263 | -47.0314 | 2025-09-01 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 42d1f0cf-14f8-365c-8e65-37626bb18358 | -9.1336 | -65.8627 | 2025-09-01 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9a4ba09a-c7b1-3f3b-9780-be1f7a1ac2f0 | -7.0946 | -44.3589 | 2025-09-01 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| adacca4a-d69a-3f64-ada0-a991565be084 | -10.5937 | -44.331 | 2025-09-01 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 6aa3ba97-fb83-3246-804b-eee01cdd7091 | -15.6916 | -48.9065 | 2025-09-01 00:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 310b163c-4628-3336-8331-45b6ac0be607 | -9.1337 | -65.844 | 2025-09-01 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| ea807c1a-753f-3ac2-bc66-3e573ba4361d | -19.0718 | -48.3379 | 2025-09-01 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 5b6d6dd2-9bff-35c8-a67c-f2baf2d0ccd7 | -14.7622 | -46.7438 | 2025-09-01 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 3534cc90-2fa5-3083-830a-195f34c9a588 | -11.3888 | -43.6312 | 2025-09-01 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |


[Clique aqui para ver as próximas entradas](README3.md)
