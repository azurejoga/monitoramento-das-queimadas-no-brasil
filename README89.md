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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bbdfce8-7b84-32c3-9afc-5933b1a27ae9 | -12.63381 | -56.99103 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29093d3d-93f0-3663-9ba5-5b2e0840e594 | -15.57699 | -50.32128 | 2025-09-04 05:18:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 866122d7-ebce-3e5b-96c0-d9f36d50e57a | -14.56458 | -48.08252 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7a53a02-dd62-372d-aa16-96f8959f8fcd | -15.18905 | -48.01305 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51baf84d-cec9-3b77-a8a0-a8b93c72329b | -12.98895 | -54.75631 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc807dcf-ae40-39b7-8d3e-90f600808c79 | -10.24918 | -61.77075 | 2025-09-04 05:18:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99e30825-fc8e-3b4b-b6db-9b240351d01c | -12.89296 | -56.9542 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1a6e67eb-5f02-3324-a9d5-436664bacffd | -12.48314 | -53.83449 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1600c9e-0acf-3ee0-a770-b20d893bab74 | -15.40779 | -55.9435 | 2025-09-04 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6bc7fd7-b50e-3f3c-a20b-e937c19e5faa | -14.53283 | -48.06532 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ab77ba0-cf88-3923-a667-bad5f0c0d7bd | -14.57704 | -54.55643 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8678e55f-6b13-3e47-b5a7-40a3ddcb318c | -11.84965 | -51.45122 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db106474-8e71-3615-959f-98fffe5a4792 | -10.58178 | -55.41725 | 2025-09-04 05:18:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b20b254-c10e-31e5-9cad-d10123480073 | -13.85049 | -47.98092 | 2025-09-04 05:18:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12adc737-8c10-37cc-bb46-9544770866cc | -12.9747 | -54.76645 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0dae2de-a37d-316d-8721-64277a4c4755 | -11.85481 | -51.49414 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fb2b869-41b1-3de2-a01a-c67b5403c479 | -13.10133 | -57.11176 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1195e673-8f95-3f34-9929-e91155f6b965 | -10.24856 | -61.77452 | 2025-09-04 05:18:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85a02ed3-073d-376e-8054-7113a7057889 | -13.94887 | -53.98841 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 183b9ca8-5bf9-3c53-a242-0d7e67874d5d | -12.45795 | -48.08233 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9c9f32c3-504a-3105-82f4-b5ed40bde348 | -11.58355 | -52.10508 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cef4fdc2-8057-3f63-9175-41061df5b4be | -11.73764 | -47.75083 | 2025-09-04 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0273fa1-2c42-3e5e-b194-9e41c87d0b85 | -16.53564 | -55.09078 | 2025-09-04 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a4967eb2-472d-3d0f-9e78-b2fbc4ef6256 | -14.55607 | -48.07508 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8e6875e-c64e-3121-8f56-8b73c3c5f098 | -11.67643 | -57.34419 | 2025-09-04 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 26404a63-71cf-3893-a92e-e119a786ac48 | -16.31843 | -52.96092 | 2025-09-04 05:18:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b23e9313-3831-30b6-9286-4ab88f7f2662 | -14.56465 | -48.05672 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85df5f4c-47a2-33f7-9413-453cef87ab2d | -14.58893 | -48.0167 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c540d2e-c51d-3424-b4aa-2a24a86fdcba | -14.56144 | -48.04935 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f0f9ebdc-3486-3adf-9700-0d058da2b262 | -11.85599 | -51.44263 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a446655-04f9-3136-ad41-6cfceef2dda6 | -15.57192 | -50.32312 | 2025-09-04 05:18:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc2f4841-306d-3154-b2b5-d35241f44263 | -11.6516 | -54.52269 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d84bbba6-6eea-3ceb-85de-6475c1e1ef09 | -11.20206 | -55.0197 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a49f72f8-877f-3f03-b5ee-cb82f31e617e | -14.93366 | -49.05806 | 2025-09-04 05:18:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5573d3cd-3641-384c-83ed-c526f80fe864 | -14.58045 | -53.02476 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecf455ac-1416-3fbd-9028-56ddfdb87c54 | -12.93446 | -48.06136 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0294bb6c-4585-3696-8136-2f8fa2d77906 | -12.9033 | -48.0442 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2314505-aeb5-3ed1-82dd-14b5a3e4395c | -10.24794 | -61.77832 | 2025-09-04 05:18:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f7e0fca-ab1a-3b21-9f08-0a197d1559e0 | -10.16297 | -61.13462 | 2025-09-04 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f752f63b-6aa8-3f4f-91e8-5017432a3175 | -11.73049 | -47.75533 | 2025-09-04 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 856568ba-dc4f-3992-86e9-f03dca0a8489 | -12.48409 | -48.08362 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4de76c7-f808-3f86-94b7-cff986e590df | -15.17563 | -52.35551 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11ecdd82-dcd7-3110-b9b0-622eeb504ed7 | -10.883 | -55.74169 | 2025-09-04 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6816b8b-78e0-3c9c-902b-3cfb644e3edc | -15.87737 | -56.89164 | 2025-09-04 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f9105dce-8799-3ee1-805e-4d6841a34f14 | -15.04091 | -50.06813 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42969850-7950-38f2-9d79-b965ac0a9129 | -12.9115 | -57.00478 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d29971d-a36d-3b73-abc7-98e5c6faf785 | -15.41182 | -55.94409 | 2025-09-04 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a61aa568-8e8c-3843-8683-8e64b67de407 | -11.57717 | -52.11557 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 997e9a00-8d4d-38a1-817e-71bb4868f96a | -15.57055 | -53.96421 | 2025-09-04 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7433994a-e508-3db0-b87f-37e8fd815ec5 | -14.20544 | -48.09641 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b448812f-46e9-34f2-8a97-180ef51e1a98 | -16.31344 | -52.96037 | 2025-09-04 05:18:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bbd616e-0fd9-36c9-a806-f3b2d375638c | -12.97672 | -54.78289 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97242534-2e32-3908-a321-3fc718d9c810 | -15.57786 | -50.32309 | 2025-09-04 05:18:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d359842f-1974-3503-83bb-046d6ad5df62 | -12.97361 | -54.77438 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aef117d9-f3ad-35e3-b18d-2ae9fda7b2b8 | -14.8131 | -48.3329 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5b7b152-7548-3d1d-9b3d-e72b11eaff6f | -15.00758 | -50.04422 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0810d64d-33f2-304b-bcfa-0b94632f48ff | -12.92249 | -57.00646 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba4f6d99-e779-3e48-9c53-93d0b1dcf08e | -12.97104 | -54.76193 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45a17eaf-7c10-30dc-ba01-360233017601 | -13.73833 | -46.91708 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9d989f27-cfba-3041-8556-1bd55168288c | -13.74988 | -46.94199 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e3b5043-7822-37d2-9f5c-c78cb54b6b66 | -15.74133 | -53.63226 | 2025-09-04 05:18:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c3b44f7-15ba-3221-9890-35192725feac | -11.65213 | -54.51875 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4800de10-e1fb-3f7f-8dc5-317b3222878f | -12.9059 | -56.94274 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3f83aaa-fe8a-327d-8041-5f7f3347a338 | -13.57116 | -48.13795 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcaa9176-8f86-3571-b1eb-edf57edc982f | -9.46455 | -62.15057 | 2025-09-04 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fc43078-c145-3d8b-b6a2-2fa7dfbe3d7d | -11.73704 | -47.7562 | 2025-09-04 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b8ecb58-1f48-34bc-b910-65864ef309ac | -14.88047 | -59.50153 | 2025-09-04 05:18:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebb507be-e4ef-3296-b832-ddb1dbce1d5b | -14.59439 | -48.02918 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc2c0a33-204b-3556-9bdc-04d47fe6e555 | -14.58529 | -53.02537 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7743b928-4807-37ca-a6e9-e5c668965e6f | -15.03974 | -48.112 | 2025-09-04 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 827cf48f-0ca9-37f9-b27b-2ad7c9a007ce | -13.10069 | -57.1161 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c78bf6f-f0d3-37b8-98b2-5a7eca1a17a3 | -10.57788 | -55.4167 | 2025-09-04 05:18:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d3b9419-79f7-330b-9863-1dc458ba59d1 | -15.18845 | -48.01886 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0d645df-3b43-3d4a-98d4-145eccd8a876 | -11.88058 | -51.53925 | 2025-09-04 05:18:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac5f6778-f8ae-38f6-b9e2-fd9874414008 | -14.99855 | -50.07211 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bace847-e6cd-3ee8-acf3-6bd79ba73ab3 | -15.30314 | -52.77451 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd39fae4-3f87-3449-b0b9-a009cdeda04a | -15.033 | -48.11202 | 2025-09-04 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54822c65-33e7-388f-abac-88d98496ebc7 | -12.49942 | -48.06435 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a35185b9-e3a9-3ba1-a863-45bc4946b8c5 | -12.49007 | -53.84299 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a221f0c-fc70-33c3-8ccc-e6d7d339e80f | -15.55296 | -48.41043 | 2025-09-04 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55d82b66-0b57-31c7-8dbe-bd2155e35e81 | -11.88613 | -51.53676 | 2025-09-04 05:18:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88c173cc-a584-386b-a040-af63a64ffd2f | -11.85637 | -51.43961 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f52c432-8e7c-35e7-88d0-42cd9d2a1c6c | -13.26719 | -51.84602 | 2025-09-04 05:18:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ff2eb82-3872-39c4-9487-1c5abef736bc | -8.88218 | -69.34484 | 2025-09-04 05:18:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65c9bf2c-6c79-35f5-8603-a5bcf2171284 | -11.60191 | -47.79105 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d8fdace-cbf4-344e-a076-71fa4a887bdf | -15.55354 | -48.42046 | 2025-09-04 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe778180-4f7d-3e5c-b5e1-55c68cdb3f9a | -11.63785 | -52.2049 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0dc35c7-fa3a-3c81-a3c2-e579c8114c22 | -12.9035 | -56.93341 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bdff28cc-05e9-3e5c-9dd4-e21710375098 | -12.89057 | -56.94485 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 69eaa952-30c5-3c98-9d3d-0bec9fbef38a | -15.24647 | -53.80313 | 2025-09-04 05:18:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2ac366f-3936-3c88-a8ef-0d90f2c1bf89 | -12.9927 | -48.07028 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00e33474-45da-30ff-b31f-3c2ba1c4757c | -14.81919 | -48.3381 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| de57d2dd-bdc2-34c9-8ba5-504ca9db8946 | -11.86111 | -51.52744 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da4acad2-60dd-3bc0-a1b3-fc699824293f | -14.54066 | -48.05486 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f49fe76a-0400-3d06-8ea0-c621bf8e8ec8 | -12.97984 | -54.79132 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e6a2205-323e-32a0-a7de-99c3312a58b8 | -12.94672 | -48.06998 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a65dac9-3ddb-3f99-9714-428ee0fb447d | -11.73109 | -47.74995 | 2025-09-04 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 417ee842-4dff-39b1-823e-ffb04e10bdf9 | -12.97198 | -54.78627 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc508ff9-c5d6-39e2-af85-2576b1eff648 | -15.02758 | -50.08028 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f872978d-82bf-3c77-acd8-896c584a9684 | -15.1761 | -52.35148 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README90.md)
