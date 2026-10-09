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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb08e2fe-4a5a-39de-8261-5bb25572ce85 | -3.2004 | -50.82936 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 111bd547-e398-3b76-95d0-b55e39279b27 | 0.52933 | -50.89948 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fd6165d0-0343-30f9-96b2-93f320bcac22 | -2.77897 | -54.08088 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 450fda02-f24d-3249-bca9-24d2d3757a24 | -1.19366 | -54.20599 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbacf034-3a3a-3ef3-96e1-f0c3fadac090 | -1.1083 | -54.17704 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9353455f-fe79-3119-83fa-a9fb7b59df44 | -3.16263 | -50.45629 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac7b9cfc-714c-3fb0-8618-768fd7e63264 | -2.21974 | -53.70183 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00eb31cd-6abc-37d1-90e8-93020b970663 | -2.49489 | -56.34297 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2381e298-20ac-339a-b7e3-a9a745056820 | -3.1695 | -50.58898 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 762546f4-9d03-3c53-8306-6164719afc35 | -2.73877 | -54.13008 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 181fb878-8cb0-331d-be7f-18a40f70a90c | -2.75776 | -54.10131 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 272c3ea4-3c95-38da-9cff-1d015aab5301 | -2.77608 | -54.07645 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc90615e-5cdf-31da-9950-5fc6433f09e0 | -2.84546 | -54.1381 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32dce514-de9b-324a-8a0c-1a7728f6dd4c | -3.69869 | -47.68311 | 2026-10-09 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b0d1415-6480-3407-8ae0-80f85fdbfc05 | 0.19203 | -51.35221 | 2026-10-09 05:01:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65bde08b-b2d6-3583-a10d-30c5ea67ba53 | 1.73434 | -55.5873 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 391a5259-d7ca-3e68-8a63-3e7bd408bba3 | -1.59063 | -47.35576 | 2026-10-09 05:01:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74057f11-4d12-3045-b6a5-7937dc8f0133 | -1.23735 | -54.20792 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cdd4007-d57b-3234-8c6a-d3393c41429c | -3.18822 | -49.24665 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9f2a5b2-94d8-391e-ac0d-3e76a3bbd2c9 | -3.16939 | -50.45734 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88af0242-19a6-3ff8-a715-6336a80524e4 | -2.48719 | -56.14095 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0f56295-af62-3458-97ee-384ade8eb6fd | -2.4009 | -51.30067 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d68f9cb-6045-3cde-80a4-d73f74be15f4 | 1.05895 | -50.03572 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c8b37c2-b14f-39a1-bd90-edcfde998913 | -2.76847 | -54.07919 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b15491da-c3c8-3cf1-9635-20618dd14b44 | -3.00918 | -51.00802 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1dfdbcfe-8e16-361b-a91d-8f85cf91f660 | -1.29029 | -55.69874 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fef5985-b1f5-30cd-9eb6-dd50a830d594 | -2.93059 | -51.48315 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9caae7fe-bf25-3930-be3e-52bb0edaecac | 1.68631 | -55.6234 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5624855d-99a5-3068-a88b-975dd302a7d8 | -3.01253 | -51.00854 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66a59d52-4cda-327a-a4f8-923d873aecab | -2.39757 | -51.30014 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1212f88d-448b-3728-ba69-0894279713c1 | -3.32779 | -50.18183 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90d7d4f7-c5f7-3969-96f6-25d7f5ea2b7e | -1.18803 | -55.66445 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9002b6c2-3bf7-36b4-baa8-ca7a4f9d7fc1 | -2.82615 | -51.28527 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17e26efa-e3d1-3160-8ece-0829b49c629b | -3.03428 | -42.10809 | 2026-10-09 05:01:00 | NPP-375D | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6c141ce-1ed7-33ba-b69a-3788f0126b1d | -2.84257 | -54.13365 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af9fa3f6-0741-3f43-9c7b-0f3bfc7e7d6d | -2.49575 | -56.16249 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 28b96c2b-fbba-3449-bd41-b1e14945525c | -0.99853 | -47.65463 | 2026-10-09 05:01:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7bff1368-e6af-359e-8b9a-09bf52de73e8 | -3.18017 | -50.58699 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a1ad60b-8a6d-31c7-9fdc-202b66b06f44 | -2.08503 | -46.57715 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| feac316a-f0f6-3ef8-a9dd-3f44de633230 | -3.17051 | -50.45016 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 500d9df8-7f95-3a4d-9415-41d05799edfe | -2.07696 | -46.57589 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b197f76-d25c-3e4c-b383-962b3a0dad61 | 0.0565 | -49.99092 | 2026-10-09 05:01:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b767f092-cd2a-354c-85fb-ec1abee74658 | -3.35763 | -50.41278 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ba0b068-f962-37e9-bfe0-ba941df540e5 | -3.279 | -50.02464 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd68a2c1-0698-3554-b757-729d0565e7ce | -2.50601 | -56.14898 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee521412-3404-3396-8702-d9f751d31822 | 1.69383 | -55.6186 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccaae265-a28b-393e-b8e7-6e3a50609270 | -2.07346 | -46.57176 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3f6dfc5-756c-3d6c-aa06-894e4b303a80 | -2.73464 | -54.1334 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4330f0a-5ad8-384a-8d4e-948fcc59b641 | -3.02959 | -42.10867 | 2026-10-09 05:01:00 | NPP-375D | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4da913f-e375-348b-93c0-e9f3960c8223 | -1.49052 | -54.53975 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f7241aa-4e21-34d0-b099-64e11a07dd90 | -2.35827 | -48.884 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f76185a9-3559-3667-808b-fc12498d28a6 | -3.21761 | -42.96474 | 2026-10-09 05:01:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db901059-2ece-3e55-906e-44a1dd194449 | -1.8703 | -53.96707 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db51cd24-c0e9-34f9-a714-ef163d7af283 | -3.48174 | -50.08889 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6612da1-8020-3a1c-85e6-c0a4b0ae5ee0 | -3.16501 | -50.59555 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 049b34d6-77d8-30b5-a101-5a7f06dec3fd | -3.25513 | -50.39718 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 849e6860-e1b0-3b33-b25e-a6b738cb70e6 | -2.76003 | -54.10962 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2962b0f5-b44c-3ae1-89b6-7da0b14a6d0b | 2.76879 | -60.00552 | 2026-10-09 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da1c3f1f-7cb6-3b7e-b981-31eb3dc5728b | -2.95611 | -51.49423 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b38932bb-fa94-3941-ba4b-a02b1bf6ee91 | 0.53211 | -50.89551 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8536fcbd-65b8-3755-a7ef-278574dd8e6e | 2.42169 | -50.81749 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59218a52-8841-331c-b7a9-1449cc86ad89 | -3.34684 | -50.481 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2bbfccc-04bc-38c6-926d-d009d4453663 | -1.52702 | -54.52038 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 238c9c0d-dbfa-3d5d-a1b1-77e6e7116638 | -3.16838 | -50.59608 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6597661-b9e6-3251-9933-ad97be77d8cd | -1.89453 | -54.67207 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b4053ab-bf39-3822-a1c2-5677c0b00c77 | -1.54359 | -54.55993 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 509c2391-f2a7-3447-9400-97f555f77031 | -2.74374 | -54.09905 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cbe24fe-a914-3e55-a27d-3a73c8305986 | 0.70133 | -51.43178 | 2026-10-09 05:01:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85bfe259-0edd-3dc8-a43a-5f83574c5f5e | 1.23093 | -52.90338 | 2026-10-09 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9fa9f7c-03c3-3999-8757-37769ed3757d | -2.99055 | -48.91746 | 2026-10-09 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63d77463-a2c4-321d-ae01-046402a44760 | 3.73388 | -51.62332 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25635436-1511-3772-8e45-e494f662405c | -4.07835 | -44.11364 | 2026-10-09 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a67e335c-8ca6-3f29-85f0-89c1509d2f71 | -2.4889 | -45.67436 | 2026-10-09 05:01:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5a9a945-bde5-3886-b5f8-85c8ed321f2f | -3.0935 | -51.37378 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c267f6f-9cea-3408-81ff-16acaaf23765 | -1.18752 | -54.17574 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb112424-caf9-32fe-a686-b8740a42d8fc | -1.53995 | -52.75846 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71b1f1d0-352d-35bb-a288-f119010614f9 | -1.28392 | -55.42057 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02a2fdcb-e922-3b41-bd00-c21c33cee9a4 | -2.39424 | -51.29962 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6eee3d23-113e-3218-8d4d-63cf93eba307 | -3.52872 | -44.33438 | 2026-10-09 05:01:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6058a2b-c582-331f-848b-79bee89f8ca4 | 2.76344 | -60.00406 | 2026-10-09 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c65fe9c-3c4a-3a10-83d3-98c5e00c7240 | -2.50914 | -56.1545 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ab33988-0b33-3370-985a-b7ef45d2b3c7 | -2.51273 | -56.25736 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75bc1fc9-9714-3519-9b82-9cac2a401ec8 | -1.41549 | -53.23026 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e3beb78-b86b-3aa4-b8a6-e0427da759dd | -2.46869 | -56.08562 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 90eef86c-8e41-337f-9cd7-efe9061027dc | -2.46475 | -56.05991 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db7ddc3f-9e0c-3e25-b543-1641dd187890 | -2.43513 | -55.97051 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9c58009-da38-3569-a645-62feaaf03a78 | -9.79783 | -44.76869 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1d90a64-53f1-35fe-b9be-94e2c7198bca | -3.65413 | -59.706 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d7b0d7a-1fa8-3282-ad25-8ee1a3465d67 | -5.98452 | -55.35762 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39bf4056-ffda-334b-bafe-bbc120d73390 | -6.48352 | -62.8528 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f148513a-e827-391c-a1ee-9b200946338b | -2.9491 | -54.19034 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4b805e9-bb45-3cef-ad36-176d5815893f | -6.46212 | -46.02325 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc839d80-6981-305a-9622-a72c532bbac5 | -7.39974 | -44.74251 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b6fd66ad-20b6-3559-8078-757e44a46e6a | -5.8856 | -43.41479 | 2026-10-09 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcbbd61c-5fd5-3f98-a3b4-de8bfb0d11b4 | -3.1097 | -53.77337 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08255c07-b8f7-328a-888f-107225a39de7 | -4.29306 | -54.80651 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43e6473b-2893-3ce2-9f8c-2e6d5e726401 | -5.96212 | -55.33716 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2781414f-ba27-3bae-9f25-14f8392db096 | -3.08245 | -54.3026 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 446e0ab0-d1b8-33df-9cb7-9be088de3a1a | -3.25449 | -54.01946 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 335242a1-1bbd-31e7-98a1-ef3550aa0899 | -3.71366 | -59.64962 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README130.md)
