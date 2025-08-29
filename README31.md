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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0950ebf-6c9f-3525-be32-188d31e7ceae | -11.29888 | -43.5424 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21ed5fd6-8134-30b7-be22-472af73d9573 | -12.81133 | -48.18682 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d05cea2-1c5e-3c60-89df-88f5f403a59c | -10.97656 | -46.90978 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 29760454-3770-323c-a16f-c70814265a32 | -6.51686 | -43.00167 | 2025-08-29 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d2f03d7-3400-3b85-a0f9-1f51d67b81f6 | -3.41819 | -49.04832 | 2025-08-29 03:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b2b83a63-a375-3a07-be99-1c0699d7c106 | -13.41367 | -46.97583 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a067a1dd-50a3-3d5f-98d9-b09020317b90 | -10.01958 | -48.07652 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d168d7b-52e4-39d9-a89e-8b669250bd67 | -11.5522 | -46.36497 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01b7278a-028e-34f4-bda8-bcbaef2ee55c | -6.23415 | -42.39693 | 2025-08-29 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6906b0dd-eef5-3571-9bd0-b80b3d6b2224 | -12.83723 | -48.16987 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d783c981-4db3-34fb-8512-370e4cd8db10 | -10.98623 | -46.85794 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a9bd245-c318-39e3-aae1-3b5301899a04 | -6.14037 | -44.43149 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75bf46d4-3f83-38a7-a4bd-c56363cea782 | -13.66929 | -44.22323 | 2025-08-29 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e605985e-9c74-31c4-86ed-cbcb995c0328 | -11.6078 | -46.20688 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c0cbe02-5731-3a0a-8d39-a1d34e96812f | -12.83986 | -48.09966 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f694bac8-99ed-3db9-98b9-12cc67ec5926 | -13.40192 | -46.84955 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a01a888-b985-3908-9f94-a7c2617e00ff | -11.05713 | -44.76823 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdec102d-37ab-336c-ad1c-eaa0cec2a6d9 | -6.03964 | -44.46859 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42918982-1da2-34ab-8cee-0a52040de548 | -11.2914 | -43.54413 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f65d7bc2-61ce-3307-9397-090d3c0ca372 | -12.91107 | -48.14164 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b5521db9-3743-399c-9e83-c4a2872de2ec | -14.24572 | -48.06467 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3610418d-0fb4-3c3b-8c31-cf2f4ec61aa2 | -14.25174 | -48.07178 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4d679ac-a716-3c8a-bc13-870816a468c5 | -11.34687 | -43.56979 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 238b9b1c-e0fc-3f16-bbd7-0a6290e9c6fb | -6.19058 | -43.32505 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54337f90-07ca-30bc-bfb1-c5c164b37626 | -11.29624 | -43.54105 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44860a67-2905-3c05-83d3-a3e3fc36aab9 | -12.92142 | -48.1489 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfbe6324-4513-31fd-90c6-41e89352568c | -6.12282 | -43.30277 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b801d8d2-899c-380d-a480-773b15e4d948 | -12.70693 | -48.19466 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1bb68e3e-abc6-36c5-a8d9-b3a3136091c8 | -11.35236 | -43.56301 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 372d5a66-7883-3b36-9b6f-5d426b83d4da | -12.82604 | -48.11198 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bf6a844-ecd3-32c1-8e0d-050d9757cf62 | -5.61929 | -45.01276 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d7bf0b4-1eab-354f-825b-488841be5bfe | -13.53406 | -46.94088 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7950bd2d-aafb-3577-8dd3-71a3b5e9b453 | -12.9133 | -48.13013 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ca412cd-8239-369e-a501-55fcb0e7ec39 | -14.24162 | -48.0577 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0048e482-4dca-3bf9-b78e-3ee1932d997f | -12.91721 | -48.13926 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 252266ef-68cb-3b9c-be5d-efc0ffce7956 | -6.16073 | -44.19553 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90280777-f0f8-357d-9313-9023fdccbd6a | -13.51443 | -46.85552 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4926fbb2-4b94-3c17-84eb-bfc9a87a102d | -10.29805 | -46.74855 | 2025-08-29 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c714327e-ba10-3276-b923-29769a91041c | -5.53677 | -36.85044 | 2025-08-29 03:49:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d704b123-e726-3d7c-bf11-7d56295ef376 | -11.87543 | -46.40241 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99c55f4a-16c3-3fda-a9d1-1e684e6ead91 | -5.79149 | -42.60793 | 2025-08-29 03:49:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 722454b1-6d63-3906-98fd-7aaeb0e6adf5 | -6.52191 | -42.99826 | 2025-08-29 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2874cf78-7113-3e46-8ffb-66d75309b0ca | -12.69531 | -48.1955 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| e26abd40-7594-34bf-ba6d-a4978c401fea | -13.52817 | -46.94448 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c4c5e2c-0d10-3e31-af83-b989a546a1ba | -5.78896 | -42.57022 | 2025-08-29 03:49:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a372adfe-d0af-3001-9406-887eb084b286 | -13.4172 | -46.9576 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c22cdce9-0a6a-309d-aa21-52ac79cf6916 | -13.17823 | -45.28177 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51beacb8-b991-32e7-bbf6-f04bda8a45c2 | -6.53954 | -43.10441 | 2025-08-29 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05263f0f-7d87-342b-926e-26701e9347db | -5.18019 | -46.07928 | 2025-08-29 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ebbb5aa3-080a-34a3-8559-7f9560bbb554 | -5.78467 | -42.56968 | 2025-08-29 03:49:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 20503170-0d57-3e56-91b9-b855eeedd9d4 | -6.31026 | -43.53254 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6a7055d-7413-3479-9c82-664be3f95c7a | -3.41714 | -49.05453 | 2025-08-29 03:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1f3e0fe3-d5bc-3a69-a2e1-e4777fcc2059 | -12.84482 | -48.10141 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25b5b6a8-d3ee-3fe1-8fa4-96a0126980dc | -13.62834 | -48.20473 | 2025-08-29 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1597ff01-3dd4-3c4c-91a9-93bc40e896b1 | -12.06556 | -46.62504 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ff5f944-dcd5-30e9-8bb8-2b767fd10b9d | -10.06485 | -46.6069 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db4eb34a-bdcb-383a-a127-297ebbb78233 | -13.39924 | -46.99644 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af136f5c-dd7f-367c-bf81-b643125e450c | -6.13568 | -45.06468 | 2025-08-29 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| accc3778-b5e4-3af4-a16b-ffff86764c2f | -13.42776 | -46.95682 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2d267d88-3593-3d66-a5fc-c80fcf0a4f0e | -13.43176 | -46.96307 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b68d3388-e8d6-3ce6-97ab-50fa083f6e61 | -11.35303 | -43.55922 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cfd692ac-f563-3f7f-9cf9-96d68d6f5bb2 | -13.18637 | -45.28818 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30830fad-0e83-3d6c-9806-3bcc42d32289 | -15.04277 | -48.12502 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 391b4a3b-c8ad-3f19-b8a8-4e08af4fbfb3 | -10.3801 | -45.1704 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ebace58-d903-3769-a100-22daee52e55c | -5.62073 | -45.01217 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14383eaa-4db8-389c-b6c4-81ad3c5f4af4 | -6.24667 | -42.39919 | 2025-08-29 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6c60d53e-0027-346c-a8b6-ada44591a703 | -12.5698 | -43.7885 | 2025-08-29 03:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1703cae7-73ad-370c-8af9-6b4247b85ab1 | -15.93957 | -49.27566 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8518fd5d-b391-31f7-a838-e655f43ec124 | -6.26284 | -43.81734 | 2025-08-29 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f39ebe9b-45eb-39ba-919f-0f1063e8c83c | -11.30733 | -43.55091 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da212c5d-37ab-3b6f-9c41-44c4adbd0f7d | -5.59513 | -45.20943 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecffd134-f76e-3f50-895a-84072cc5c351 | -11.26143 | -45.50108 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17297fe7-420a-399e-b0ac-daed119b81e3 | -12.69088 | -48.16133 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dcd4ee0-0160-3d4a-a622-f283ce888508 | -13.55849 | -46.89482 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6a50c85-5c85-3f39-9075-7ab4c406bc2f | -17.75522 | -44.50481 | 2025-08-29 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a3ca7398-9ef1-3e40-8836-6f0374fa14cc | -17.04184 | -46.50392 | 2025-08-29 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da49431a-4f01-3ac8-9cc4-c04198f106b3 | -13.58998 | -46.8652 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ada0663c-60cb-30b8-a4bc-c4c3e6d6438a | -11.56403 | -46.32991 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed984cf1-8e09-3c7a-ab97-00c5fbf7e15a | -12.90594 | -43.57323 | 2025-08-29 03:49:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e54b4085-9047-3dde-b320-202d0d71c393 | -17.85282 | -41.54025 | 2025-08-29 03:49:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aacd1b20-2869-312c-ac00-996d1e447fd0 | -14.04017 | -44.48387 | 2025-08-29 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db580392-d45f-3a31-8245-2fbb9c7b8f33 | -15.83529 | -41.85331 | 2025-08-29 03:49:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d2e80c9-98a3-3dd0-9760-49fa04657a92 | -12.92682 | -48.15032 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f54fbdb-084e-369a-960b-b32b9b3dfa32 | -10.36883 | -45.17881 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8481250-52d0-37bc-ab65-796eb6371eef | -5.79327 | -42.57065 | 2025-08-29 03:49:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c4de40d8-88c0-384b-ae82-089a98646983 | -11.3537 | -43.55541 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4861751-27da-3691-97ed-7481614cdc12 | -5.62139 | -45.00086 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e4dca5b7-e8ef-3e31-a63c-f929acefe355 | -5.78788 | -42.60321 | 2025-08-29 03:49:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8e8bfd0e-122b-33c7-a6be-b76efc8ca425 | -5.53866 | -42.63967 | 2025-08-29 03:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 21b174db-3b06-39dd-b5d0-0f0b2016af43 | -13.63374 | -48.20587 | 2025-08-29 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d536bafc-dc6a-31e4-b78d-ba8a70656ddd | -6.49044 | -43.52801 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ee7e12e-88c2-32a4-b4b5-0a0529781b6d | -11.95479 | -44.84667 | 2025-08-29 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8332c5be-625e-3235-9374-ffe17dc58a9e | -13.64154 | -48.16646 | 2025-08-29 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9586dfd-42b8-3c16-9e78-4ad5da9e7793 | -14.33138 | -48.65375 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3239f33-f95d-3678-bcd3-5373e3222001 | -5.61685 | -44.99713 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d18c50e1-5a4e-36b0-a161-dbe971c401ef | -12.83302 | -48.10549 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e8b6bc4-da79-3594-95e8-0153c83bc793 | -13.57018 | -46.86084 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a0eb2a4-8806-3f16-b8e8-7ee34ac3b720 | -14.90157 | -46.45396 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e43004ff-277d-3d16-8efa-040ebcdff1ad | -6.49419 | -43.5332 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca2a45f2-4993-30ee-b824-2f6f90d9aab4 | -7.56263 | -37.18635 | 2025-08-29 03:49:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
