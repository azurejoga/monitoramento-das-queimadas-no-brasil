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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8120c449-63b5-3346-90b1-5f31bf6a3488 | -14.01707 | -55.12912 | 2025-05-16 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1965224a-7406-398d-b714-589129d74756 | -13.60207 | -47.37944 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ed9939e-c23e-3fe2-b10c-59ddc7e49ba7 | -13.28151 | -45.41602 | 2025-05-16 04:36:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bcf9e53-15fe-33b3-ae9a-18d072e8ca55 | -14.17873 | -45.47693 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e02cd0e6-962f-33a0-9904-12997ae1a6e8 | -13.95916 | -56.79614 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb41bcdc-9eff-3d44-b437-adf0adc15fad | -11.30394 | -54.01208 | 2025-05-16 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8c051de-8f28-36ab-af86-8e2f3beed1c5 | -15.78279 | -54.51588 | 2025-05-16 04:36:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cb1b0e2-2b4f-32ac-a9cd-31c6fb6e3374 | -14.17429 | -45.46816 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a9dfb6cf-1645-34a6-a235-4c035da8d846 | -13.61876 | -54.88472 | 2025-05-16 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9428470-2d39-3ff5-b77a-2b554056d1f4 | -11.56298 | -47.87671 | 2025-05-16 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a49a97c5-8a69-364e-9b1c-a45f72cdf840 | -14.17244 | -45.46615 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6751979-d2af-3b47-911d-90e7440bea99 | -14.46972 | -56.3183 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce873434-0348-3b60-a924-d17cee1354bd | -14.16723 | -45.47522 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97fcef50-adc7-3cdf-8724-d13b81de14a5 | -11.96237 | -63.52457 | 2025-05-16 04:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 21c4b98a-abb5-3efd-a734-097000431cce | -11.30795 | -54.01279 | 2025-05-16 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96dc7f7d-a233-34da-b9b3-ed48f7faf25a | -15.26986 | -51.46703 | 2025-05-16 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fec82d72-58e9-3c42-8d2f-76510a30c1f6 | -11.38744 | -57.8219 | 2025-05-16 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3815b94e-055c-3379-8f59-c7875a2e11fb | -13.58766 | -47.38085 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f16cae7-a64e-36d2-9f64-021ea0f40108 | -12.68141 | -58.12932 | 2025-05-16 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 479f9b25-1fc1-324c-83ac-937398b04dab | -17.05978 | -45.92283 | 2025-05-16 04:36:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b90e19f0-4229-3349-b05d-cd2c0a23b606 | -14.86991 | -51.98209 | 2025-05-16 04:36:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2201ce8-36de-396b-910c-07274dd77621 | -13.04433 | -53.72092 | 2025-05-16 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ed22c2a-a1d9-3412-9c9c-ef8a19ac3199 | -14.01641 | -55.13287 | 2025-05-16 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 424cb25e-c2ac-35f8-b297-3958b6774ec6 | -12.87251 | -55.06133 | 2025-05-16 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e55c8854-a799-3103-bd13-ef736a564445 | -11.58414 | -47.61956 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff4e8a56-ea41-31be-bbd2-c04ab9aa5bb3 | -12.16542 | -48.80641 | 2025-05-16 04:36:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b80774bf-aace-3e6f-9b91-f01d36054cc4 | -14.46891 | -56.32273 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 489a2335-7d29-3bd8-8180-e869ecf11f70 | -11.2935 | -53.9767 | 2025-05-16 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6581f29-6c4a-32af-8413-fa8706bd7f1a | -14.17804 | -45.48174 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eace44e-4682-3d10-8808-4885a0015586 | -13.08372 | -47.80881 | 2025-05-16 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b64eec4e-a28f-3015-abaf-a0aeeedd42e3 | -10.5154 | -59.3839 | 2025-05-16 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fe9f634-498b-34ba-94c3-106baa2188b6 | -14.17489 | -45.47636 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e03f62a-9866-3578-9363-2936c81fa747 | -17.25113 | -48.11467 | 2025-05-16 04:36:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9286f66e-06e8-3f69-94a4-efd17e8750c6 | -17.66429 | -46.6862 | 2025-05-16 04:36:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6adfaee-f649-3ebc-8ae9-32d772647ea7 | -11.39282 | -57.82374 | 2025-05-16 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| beac1aa7-6abd-363d-a57c-2b08e42e31ef | -11.96208 | -63.51934 | 2025-05-16 04:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 986b180c-3cec-3365-bf62-7be4cb2e23b2 | -11.57168 | -47.61013 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f85f1241-9063-3f2c-b596-2e74b82a041f | -11.38767 | -57.82276 | 2025-05-16 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd63a568-0e70-3243-b08b-82e556f446e4 | -11.62856 | -48.47035 | 2025-05-16 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d45839bf-b3ff-3442-934e-155b64ab1948 | -12.45261 | -57.21262 | 2025-05-16 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60617ff4-7b76-3c00-b352-2bd54e5fd4e0 | -12.45605 | -57.20852 | 2025-05-16 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9554bbc2-8251-311a-a5e1-f12f0584638c | -12.45711 | -57.20301 | 2025-05-16 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7eca35b4-39af-36b3-84db-c42d9ed58469 | -13.39621 | -47.5064 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d46058af-2f86-3126-823d-f293ce828719 | -14.01362 | -55.12461 | 2025-05-16 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 494588b4-7e92-398e-938a-7820d8c0ac3e | -13.67393 | -47.97333 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1274709-dd57-396c-9202-62304667daf2 | -11.96054 | -63.52667 | 2025-05-16 04:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3da15d85-9078-3c3b-ba3a-548f54cae5d1 | -11.78497 | -47.35946 | 2025-05-16 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99bba125-2d93-3b4b-8469-3abbfd1478f2 | -13.96284 | -56.79356 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f496abc3-348b-3dc5-80fb-1f54e299079d | -17.05657 | -45.91726 | 2025-05-16 04:36:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f99e5a0-a07a-335b-be2e-69dc9b4a84f6 | -12.16209 | -48.80587 | 2025-05-16 04:36:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fc478f7-5152-3c87-9be1-00d052f4575a | -14.17615 | -45.48321 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dca6c041-0eac-346d-8609-6f7c356fcb63 | -17.25172 | -48.1107 | 2025-05-16 04:36:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 467dc698-874e-31cd-b45e-e61c4f75f1e5 | -12.72359 | -54.97223 | 2025-05-16 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c7b5c48-630e-3469-90d1-bd72e8aeebc7 | -12.33871 | -50.32679 | 2025-05-16 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d08c3b2-6a03-3f88-b783-f036263753b2 | -13.0405 | -53.72019 | 2025-05-16 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f551e92d-8249-3cd1-8388-01ae09213340 | -12.68597 | -58.13338 | 2025-05-16 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09e54abf-db6a-3eff-9684-d936494cf6f8 | -14.18447 | -45.47952 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 072b6da8-5aa6-3a47-9c10-6e4014952f20 | -13.95731 | -56.79758 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ebbedbd-68e6-3555-90f6-9d30b2703d0d | -15.26246 | -51.46959 | 2025-05-16 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a508dfd-ef39-30be-af2e-9cd73d622228 | -11.61376 | -48.01807 | 2025-05-16 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77203ddd-aa9b-3aa4-95ef-688fa314e3d6 | -13.60497 | -47.38388 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ff1c87c-6aa2-3135-94cc-870b0991044f | -13.67051 | -47.97286 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7d53008-4ec9-3625-b6fd-afc517449175 | -15.26647 | -51.46643 | 2025-05-16 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96e11e22-cee2-302a-9ed3-94bd176a199d | -11.7821 | -47.35519 | 2025-05-16 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b017bb42-c56f-3474-bc2b-e2f261030159 | -11.71357 | -47.73884 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dce7ec05-82e4-3234-a9c6-cdb57730c48b | -14.17558 | -45.47154 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 590c08ef-0b7c-3b85-a292-09a446708349 | -14.17363 | -45.47299 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 635faa9f-d537-3c8a-a718-976a812b4905 | -13.67222 | -47.9616 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e36e4c8-964b-34ba-9954-00f43049fc99 | -13.95827 | -56.80099 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecc9b80d-3f88-3736-ae26-ecdea7d0dae9 | -12.44758 | -54.39133 | 2025-05-16 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dceb4e3-be0c-3bec-a914-2e3531a1011e | -14.17297 | -45.47782 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b679d97a-dbd4-32ea-8204-3321a728d182 | -12.34625 | -49.95939 | 2025-05-16 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0174f80-c8ad-3fbd-95fc-e6e795c1beae | -17.11073 | -49.14155 | 2025-05-16 04:36:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e71b4cf-f7de-301f-86a7-0778d9e4802e | -14.1813 | -45.47412 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ea19318-1cbd-3c21-b2ca-806123fae645 | -11.51279 | -48.57994 | 2025-05-16 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f083dd4b-eb2d-3348-bf0c-0c47cbbeafd1 | -11.61712 | -48.01861 | 2025-05-16 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e9841be-25a4-3060-b0b8-d7f3c4a9ffea | -10.52123 | -59.38477 | 2025-05-16 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 377e5734-ad88-31f7-a6e9-ceeae1b843c4 | -13.38901 | -48.44811 | 2025-05-16 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83f57282-5d02-3c23-abf4-74a440bee54a | -11.57791 | -47.61485 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f793da90-b4e2-3d79-bc6a-1662be64e278 | -11.42245 | -54.32833 | 2025-05-16 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1a0eeb9-acf9-3748-9a46-3917a43c507a | -17.25159 | -48.11451 | 2025-05-16 04:36:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b734c8ac-4785-3dc4-86e8-434952c2270b | -11.38825 | -57.81973 | 2025-05-16 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5982eec6-f9da-3b19-9142-a021728ab58b | -11.58075 | -47.61905 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4cbe219-1e77-3aa1-823b-80c94598a2e3 | -10.39575 | -57.54158 | 2025-05-16 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 794cc48e-b847-3779-8e25-7824977b3142 | -15.26925 | -51.47076 | 2025-05-16 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40e03de2-30dd-3191-a4c1-33dc5b40eb18 | -14.18064 | -45.47896 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b91e3821-da57-3897-831a-b54a48f893c9 | -11.30454 | -54.00856 | 2025-05-16 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d4073c3-09ec-3510-a42f-b62517dd9b71 | -14.18256 | -45.47749 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9d3cc0c-58f9-3d3b-98f9-1bf6ca2f8fe4 | -11.39223 | -57.82681 | 2025-05-16 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6071c1fc-127a-3eef-bcea-70e7a6c00141 | -12.33813 | -50.3304 | 2025-05-16 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56710e1f-0146-3482-8d99-ff8b974a67c7 | -11.58433 | -47.87262 | 2025-05-16 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aab5d7df-386d-3ebe-88c9-5396bd6b4bea | -11.57564 | -47.60699 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0aa4278-d5d4-3972-93af-18aba0cf1d8d | -14.01296 | -55.12833 | 2025-05-16 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb13f942-2324-3bbe-be45-146f464f3955 | -14.47332 | -56.32364 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3559bce4-565e-35af-8011-a088608b57d4 | -14.63959 | -49.2939 | 2025-05-16 04:36:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7211af8f-ee20-3d24-9edf-a30e88374b0f | -14.0193 | -50.71072 | 2025-05-16 04:36:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 615adc9e-9492-3539-bd3f-03866e5e3067 | -10.39117 | -57.53757 | 2025-05-16 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4051a28-749a-3d3c-b87b-111a4c174e7f | -15.35598 | -53.08606 | 2025-05-16 04:36:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11639050-0957-321c-a9d3-143dd75bfe62 | -13.59169 | -47.37762 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f1d4086-85d9-3106-a299-6a498d30a25b | -12.16264 | -48.80233 | 2025-05-16 04:36:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README9.md)
