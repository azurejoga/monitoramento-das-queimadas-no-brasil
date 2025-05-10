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
| e55df56a-9470-3e13-bb09-b6a657e54f00 | -13.62194 | -54.88692 | 2025-05-10 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 818a5c4f-9c70-3f08-bbab-e87d332a27e9 | -18.19085 | -45.63282 | 2025-05-10 04:21:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de77a2db-f0d1-3506-8024-a04b7d33c4d0 | -13.24923 | -50.13184 | 2025-05-10 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 87a178b5-9c7e-3f31-af47-5391398ebe2e | -16.68003 | -43.88616 | 2025-05-10 04:21:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ad78a4d-17d4-30cf-8df3-8d430e6a1124 | -14.64718 | -45.12879 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fae2fef-4130-34f6-914a-591a7650637f | -17.30017 | -47.01104 | 2025-05-10 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e7d5915-8f02-3e15-a7d2-e7a618b67d58 | -12.6432 | -54.06892 | 2025-05-10 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 424bd5df-db77-3b30-a3d7-131f2b288ddc | -11.14422 | -54.22815 | 2025-05-10 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 715ae6c4-7bcc-32c6-8cb9-9524308da05b | -14.64533 | -45.12839 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c75a3f6-47dc-3677-93ec-56f6b523acc9 | -13.62181 | -54.88368 | 2025-05-10 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7176dcee-34dd-3c53-abc2-58f2cc130520 | -14.64309 | -45.12049 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce1349dd-4380-362b-b974-be3c4452f190 | -11.39071 | -52.94229 | 2025-05-10 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5488624b-5e26-3bc0-80af-973197c81259 | -11.41077 | -48.71228 | 2025-05-10 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea845969-a349-398e-9594-b2cb5601f551 | -11.1444 | -54.23139 | 2025-05-10 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d4094df-a12b-3f07-9bd4-90095d014f82 | -12.11507 | -47.98041 | 2025-05-10 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db1edc3e-8f6a-3480-bae9-6fab9708f1f8 | -13.04794 | -53.72662 | 2025-05-10 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b2218ea0-c39c-334c-ad53-d4895209279f | -13.62252 | -54.88385 | 2025-05-10 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a316835-a625-309b-b857-863eb236a096 | -12.64908 | -54.06429 | 2025-05-10 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9933e79-bdb5-3a1c-b7cf-7f8915d9f5d1 | -19.41894 | -44.3418 | 2025-05-10 04:21:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a1a4989-b180-31cd-96cd-77084f44205b | -16.0409 | -43.81028 | 2025-05-10 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52f3b92a-0521-33ba-90fb-4cbc1c8cb5a4 | -12.68345 | -44.33101 | 2025-05-10 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 946f6627-4c02-3b20-b916-f801e59c85cc | -11.62058 | -48.12351 | 2025-05-10 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90ebddda-c9be-35e7-b9bc-3c8b536c12ae | -13.04888 | -53.72153 | 2025-05-10 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7c02da10-3729-3f03-b8ad-f0b98217d7cf | -14.647 | -45.11734 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8773b0b-298c-3c15-83e6-5246d0396685 | -12.17182 | -54.2372 | 2025-05-10 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a427b8a-05ef-3de2-9d66-8d88016d662c | -18.59714 | -46.5527 | 2025-05-10 04:21:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cb299e0-708d-3e96-9d93-fd2cefa6c5bf | -15.03799 | -45.64942 | 2025-05-10 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3660676c-08c0-36df-80e2-ce6f26d75d03 | -11.78007 | -48.6974 | 2025-05-10 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cd2903f-895b-30a0-968c-2e199b56d959 | -13.97491 | -56.80495 | 2025-05-10 04:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d86da4a4-d24c-3250-939e-d07d3c054c1a | -11.38586 | -52.94018 | 2025-05-10 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 74d739b2-8d5c-3c25-bbf8-20610f2e5bf7 | -16.11137 | -47.5582 | 2025-05-10 04:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 420e1120-c4d6-38f3-b059-bf7b1d338552 | -16.30403 | -53.83264 | 2025-05-10 04:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c473d9c4-d483-3e50-8c21-818f026b1adb | -17.30347 | -47.01159 | 2025-05-10 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdc11e2b-3335-36dc-bf16-2a9c7b4786d5 | -15.04963 | -45.64022 | 2025-05-10 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bafee235-8bc1-33e2-9842-df8d2a50d143 | -11.38105 | -55.12192 | 2025-05-10 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fe06cc4-0677-3c71-b82e-ee629166ed2d | -13.08759 | -52.29266 | 2025-05-10 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bbaf42c6-6734-375d-8af9-fb18028baffe | -17.00966 | -49.77981 | 2025-05-10 04:21:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f5d3ecc-d244-3744-9b62-3efcaf4f0ebd | -11.83282 | -51.34011 | 2025-05-10 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27ea3827-acad-39c0-ad50-977563500194 | -13.25295 | -50.13251 | 2025-05-10 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 94252b3a-64c4-3de1-abfc-67d0a6053b27 | -12.63836 | -54.06801 | 2025-05-10 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0ccb9b4-52f7-30a1-a887-939681f0eb26 | -11.37576 | -55.1208 | 2025-05-10 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10fd7263-3b3d-37a3-829c-2efa35d37059 | -18.14849 | -47.80276 | 2025-05-10 04:21:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30e2bcef-38fb-3528-a7d1-5a9efba91cdd | -15.79234 | -54.52348 | 2025-05-10 04:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5733125c-f2f7-344d-b03e-27c3b6d915d6 | -12.63351 | -54.06712 | 2025-05-10 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02019421-4a1a-3c49-b70d-88e3f0be5b45 | -13.98051 | -56.80631 | 2025-05-10 04:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 024b09ef-4c5f-313d-967a-ca83f9d8300f | -11.39045 | -52.94103 | 2025-05-10 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16f65124-84ad-384b-9e48-bf1f64fb00a2 | -18.50028 | -47.5994 | 2025-05-10 04:21:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89ddb4b2-ceee-3365-a5c2-c68d3513b7a3 | -16.11583 | -47.55156 | 2025-05-10 04:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f4ee08e-30c4-3737-9e81-766e4faeef31 | -12.68684 | -44.33153 | 2025-05-10 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d4785f1-5889-3341-ab4e-68f7e0d14165 | -13.37845 | -54.2597 | 2025-05-10 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1623b9f-8857-3f97-a2ac-a7465a294dd6 | -12.72645 | -54.9733 | 2025-05-10 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ee64820-5a2d-365c-b978-63a1c8aefc57 | -14.64589 | -45.1247 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc420706-1d19-3b4f-af3b-3383ab4b0ba4 | -11.77587 | -48.70085 | 2025-05-10 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25a7709a-b680-366d-b8b0-9ff3bad6f939 | -13.62121 | -54.88674 | 2025-05-10 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faab1a43-0934-3758-9e01-539b21d950bd | -17.53289 | -52.11802 | 2025-05-10 04:21:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6bb67e3-63c6-32c7-ad1a-993a18d97388 | -11.38612 | -52.94143 | 2025-05-10 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d81bb77d-1063-3bdf-815c-fb5375c675bd | -12.72586 | -54.97643 | 2025-05-10 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9ca68e5-53c5-3401-9171-d0c1fc2ac77d | -13.45491 | -46.71429 | 2025-05-10 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea413498-cb09-3bd3-b994-dcdd012f0351 | -15.43221 | -48.01257 | 2025-05-10 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87fc1716-aa6b-315a-a68d-857825a2ec52 | -13.97968 | -56.81043 | 2025-05-10 04:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c6c2c2b1-70ef-335f-8b2f-7ba85887c13e | -12.2647 | -49.31381 | 2025-05-10 04:21:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20c42feb-cbe3-36ec-b7ba-04ab3a95c89f | -13.3774 | -54.2653 | 2025-05-10 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f785f1e-8d81-3fb0-82d8-83d1a88c3eeb | -17.75218 | -42.89637 | 2025-05-10 04:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a13effa2-bf06-3df6-ab5d-08e39ae6671b | -14.64609 | -45.13615 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 357971c7-b1e5-35b8-9fbf-2c8f930bc559 | -15.60734 | -42.65678 | 2025-05-10 04:21:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2818d5b-a774-3f2c-8c59-ce0c3d56c695 | -11.40333 | -52.94841 | 2025-05-10 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ed277e24-63a7-39f4-8958-c6a114186735 | -13.68069 | -41.89846 | 2025-05-10 04:21:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7ab65975-befb-3c04-9e56-28307ca67492 | -11.61995 | -48.12738 | 2025-05-10 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed18d6ee-475f-3359-8808-2d7986021416 | -13.97888 | -56.81445 | 2025-05-10 04:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 14e284ec-0971-3747-9903-1ebb787d3225 | -13.0442 | -53.72055 | 2025-05-10 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6f6fcaa3-7814-37eb-8fcd-afd1861101b1 | -14.64253 | -45.12417 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a29e855-4495-31c6-8629-590d73ae3ac9 | -19.43904 | -44.33895 | 2025-05-10 04:21:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c8b749d-163e-30c8-9585-a14551c0dcb7 | -14.64945 | -45.13669 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cef6582-2998-3a0d-b63d-23625baf343c | -14.8575 | -45.19879 | 2025-05-10 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e3a36f7-220d-3c55-84f8-bbe5fb4f5955 | -12.64805 | -54.06982 | 2025-05-10 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07791114-0cce-3e0a-8921-a8dbd143d924 | -13.59999 | -43.89312 | 2025-05-10 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 779295b1-45bb-393c-98ee-88e51929f61e | -14.6489 | -45.14037 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3026faa-cf51-34ea-b8f5-0b1114c4d86c | -13.0926 | -52.28931 | 2025-05-10 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2ca9efbc-5f27-34ac-acb5-fa9cc0d1cd37 | -11.40702 | -52.95415 | 2025-05-10 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 53c67a8b-2f1e-3033-bfce-762e49e8923b | -23.73751 | -46.77375 | 2025-05-10 04:23:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 201af511-1292-38bb-af67-332b5e9ee741 | -18.96002 | -52.25537 | 2025-05-10 04:23:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6df1afb5-2647-3c21-9bb8-c46b90ff1e1b | -20.41826 | -43.55524 | 2025-05-10 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0d02533f-4a0e-3687-adac-206575e44faa | -22.67542 | -42.8553 | 2025-05-10 04:23:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8a53fd1e-0aa2-38ee-b4aa-575b1940b9d0 | -22.90398 | -43.75869 | 2025-05-10 04:23:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aeac20cb-4fde-333a-8f33-4b661582c5db | -18.95909 | -52.26048 | 2025-05-10 04:23:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 628541e3-f68a-3d0b-885d-6a852b330349 | -23.0638 | -46.64148 | 2025-05-10 04:23:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| df1d16de-773e-3bf1-8564-4f00c0958555 | -22.58829 | -42.09906 | 2025-05-10 04:23:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a7390a46-c00a-3f8f-8925-2697a50fc6f3 | -19.94649 | -44.71917 | 2025-05-10 04:23:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 88a7387f-82d9-340e-942a-0f3bf170d67e | -19.97025 | -44.21593 | 2025-05-10 04:23:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b3c8ab3b-7f71-3b17-8788-709ee03f4801 | -22.59207 | -42.10402 | 2025-05-10 04:23:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2b295c93-8d40-3e7c-8857-564335539333 | -20.31216 | -45.58262 | 2025-05-10 04:23:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeee8728-bf0c-3112-abc6-404b1056488c | -19.06002 | -53.45434 | 2025-05-10 04:23:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3b453d3-0a0c-3258-a023-ab71afba1da8 | -19.20615 | -47.69788 | 2025-05-10 04:23:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24bc1f9d-8605-3657-88f8-5a9d08958af2 | -20.9838 | -43.03524 | 2025-05-10 04:23:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6e5c9b41-7159-3455-9404-3e76f10f7f4a | -21.19674 | -41.3059 | 2025-05-10 04:23:00 | NOAA-21 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b701715c-9f34-3fd9-82d5-73c24e2e81fe | -19.05587 | -53.45355 | 2025-05-10 04:23:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 138f9167-2736-3a8a-aee5-99290f6764ba | -21.38277 | -48.52253 | 2025-05-10 04:23:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6955088-52ec-36b6-ace7-f80c69f35d26 | -19.06416 | -53.4552 | 2025-05-10 04:23:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98546e97-e635-3edc-b57e-69eda86c32b3 | -21.20116 | -41.30658 | 2025-05-10 04:23:00 | NOAA-21 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8cae9a2c-36ba-3c47-9c58-099c4bb12880 | -19.98124 | -47.19345 | 2025-05-10 04:23:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README5.md)
