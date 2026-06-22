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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d242c6ce-e469-3fcc-9c65-06baf22e9bbc | -14.63035 | -54.45272 | 2026-06-22 04:25:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13b79388-8a67-3ba8-aa8b-ca58e7fd34e1 | -13.2978 | -45.21019 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc9035fa-b5c9-3d4c-850f-06af413f8d31 | -16.23366 | -40.13433 | 2026-06-22 04:25:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 560e2e0d-6a9b-3e48-8f5d-0e08b4398e16 | -11.05008 | -52.48124 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e44c92ce-b3ff-3f55-8746-a47203380799 | -16.02873 | -43.42027 | 2026-06-22 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69168a87-3a6d-3bb0-8f68-28306abbd2e0 | -11.10521 | -54.13887 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e21cfbd3-f041-3543-a554-f27036bc848b | -13.5234 | -52.16543 | 2026-06-22 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 778db64a-f664-3202-ad0f-a67298b29bc5 | -10.5382 | -47.72775 | 2026-06-22 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 60e666de-a974-3035-86b4-297851be8723 | -10.17387 | -51.66256 | 2026-06-22 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69f13db4-0330-3f1b-bc8b-823b54ec33f3 | -12.43099 | -58.41358 | 2026-06-22 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b1a74cf-e55e-3b9e-8537-76243f579c99 | -14.10941 | -49.87881 | 2026-06-22 04:25:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54240780-5b9c-3749-bb4d-0f1d40a9616e | -11.11401 | -54.14672 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5eee6605-2e19-3fca-acd3-3328fa0e438e | -13.37324 | -41.35122 | 2026-06-22 04:25:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 682e60db-c667-392c-a85c-bfa86611756d | -12.20061 | -47.97074 | 2026-06-22 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8c88dbd-e664-3c28-87b0-a008bcea4517 | -13.84003 | -47.12132 | 2026-06-22 04:25:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3986f63-3836-374a-b066-33a4ace8bb9e | -10.94403 | -46.42356 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93fb0b38-12c4-3ab1-8da8-7154e7ba67cc | -12.85022 | -44.39614 | 2026-06-22 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60cfbc29-a1e0-381a-854e-2bf3bde841ea | -13.29167 | -45.20549 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b4743d7-b62c-3c53-b50b-59c87c10883e | -10.56695 | -46.23199 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b970917-f4d8-3a82-a696-f7b4e61638e1 | -12.06572 | -48.42487 | 2026-06-22 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a51b847-bfdf-32ab-b371-cd427b42c3c8 | -13.29277 | -45.19826 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 192a02cc-df5d-3dfb-8159-c67e3e21da65 | -13.51851 | -52.16862 | 2026-06-22 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0edb3ea-9dd3-3624-a70d-b7f7d3e7284e | -11.05899 | -52.48282 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b11b723-f8a7-363a-8b8b-7ec2ccc7fcda | -10.53899 | -49.46598 | 2026-06-22 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba2b38d1-9aaa-3a8e-80f0-a4acce3ad3fd | -10.56307 | -46.23496 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1dfeeb8-029b-392e-85dc-67c7ce412162 | -13.30173 | -45.22933 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90dcf19d-4ff2-336e-bafb-4f436d362038 | -13.29556 | -45.20242 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c614ec0-ccf9-33a9-9d6b-41406ce173e5 | -12.43569 | -58.39915 | 2026-06-22 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d13e2df-e033-3cf2-8859-68ed81134ea5 | -12.42521 | -54.18054 | 2026-06-22 04:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 498d6842-b8f4-3db4-8dc8-88aff693f5d8 | -14.79933 | -48.9588 | 2026-06-22 04:25:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb843b9a-a272-3214-beb6-dd9a2b93a5c0 | -10.55864 | -46.24144 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef64ebaa-8859-3565-b3f7-1931dff314a8 | -11.0517 | -52.47219 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8af6219c-aaef-3098-8138-3c6497afd5b5 | -10.90743 | -46.31348 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fc113ab-2d9c-3deb-89a1-5fd498b7bd13 | -10.254 | -47.34396 | 2026-06-22 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f021dace-575c-35da-a8d5-643e2c8f951c | -12.42712 | -58.40844 | 2026-06-22 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d2bf36a-e1e6-3362-9349-4d4cda9529e7 | -12.20123 | -47.96698 | 2026-06-22 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd24008d-1a52-3c96-9ac3-2635a9feb286 | -10.17815 | -51.66332 | 2026-06-22 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c77f2daf-0e79-3dce-996a-998d5997ddc7 | -11.04926 | -52.48578 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0952df68-bfc3-3d08-85ae-5b76ea01b3af | -11.25334 | -41.90472 | 2026-06-22 04:25:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 30c24b0a-3400-3f0d-a6b0-e070f2f9a0cc | -11.04724 | -52.47143 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbf8465b-ce98-3d88-b771-2f909add118f | -17.21845 | -43.67689 | 2026-06-22 04:25:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9a1bbf30-3305-3d58-aaa5-974b32e87a13 | -12.22576 | -57.28548 | 2026-06-22 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c83b289e-13a3-31b0-8269-3dd91f7b7733 | -10.77032 | -54.10756 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 343cc01d-592d-37ba-9cb1-0a0e244fa0bb | -12.32514 | -43.44664 | 2026-06-22 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b2b099c-4a57-38ce-90a5-53c391dc94bf | -12.43316 | -58.4029 | 2026-06-22 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d104464-a018-3908-a576-5c271f9fd5f6 | -12.46891 | -55.13622 | 2026-06-22 04:25:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a279dcda-f67b-3d46-bb6d-facb1af3a47d | -11.05454 | -52.48199 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4169e4ad-1784-34ff-8550-fdd7abcc831e | -12.21983 | -57.28414 | 2026-06-22 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52fefeb1-4c7f-3387-bffd-e17a4f87bf8e | -14.63071 | -54.45038 | 2026-06-22 04:25:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49dcffec-95ea-396c-9cc0-d8254bde8537 | -13.30562 | -45.22626 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a8ee925-0c95-3292-9e16-0332e0eebcd9 | -13.84163 | -47.13255 | 2026-06-22 04:25:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d60b3fe3-6584-3536-96f8-53b2510350d2 | -13.28943 | -45.19771 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a8e6752-60a9-33c4-a539-e581ac5356a6 | -16.0257 | -43.41527 | 2026-06-22 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4598a1b-db39-391b-bb33-fd0499cd39a6 | -10.55976 | -46.23442 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52657454-4cef-3d88-8e82-f67666912182 | -11.09418 | -54.14266 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69b48b3e-8cfc-3aff-b240-472f726065de | -10.91018 | -46.31753 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab071ec8-92c2-367c-98f0-6f61b472256d | -11.09915 | -54.14363 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 494adf0f-9c6e-37bf-b858-fd6e32a4d529 | -13.52756 | -52.16631 | 2026-06-22 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a4c642b-1c64-3386-9ec1-10cf8628862a | -11.05373 | -52.48653 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 842b537c-2a62-3084-b890-d808a60baf19 | -13.30283 | -45.22211 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2f72029-ef84-3615-b6c7-b3a5c7fbdb21 | -13.30339 | -45.21849 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99267c6a-fd94-3fa4-9f76-a0d3732780fc | -13.29838 | -45.22879 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59a823a6-c8e7-35a1-94ce-c8a958c7a037 | -11.1063 | -54.13311 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73dc4ed6-45a8-329f-9ee8-2a666e32907f | -10.05708 | -48.09205 | 2026-06-22 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 462ed555-a435-3b2c-a270-8e0e24f578cd | -10.57026 | -46.23254 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f9c3190-4224-32fc-8d60-5042ba3bc730 | -13.30004 | -45.21795 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f04e070-044f-3c41-b8da-a3794f0aa17c | -11.09527 | -54.13695 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc51a22a-df33-33b0-a67b-56ebfc2c96f2 | -13.29836 | -45.20658 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ea4c313-38c3-3139-8eb1-a4fd002d5be4 | -10.05772 | -48.08813 | 2026-06-22 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98f370cb-f6a4-3917-9f63-334c34493816 | -13.83671 | -47.12079 | 2026-06-22 04:25:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abb3f0de-9e76-37ca-b8d1-ea9a70c1d63f | -12.43426 | -58.39748 | 2026-06-22 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e211ac40-3787-31f7-beb3-a365587ddea5 | -13.51433 | -52.16785 | 2026-06-22 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67b16e0a-97ee-39b8-b7ac-e8d4d8819de0 | -13.5616 | -43.5088 | 2026-06-22 04:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 216c04bd-475c-3bad-9a7a-ce1653ded10c | -12.46456 | -49.15919 | 2026-06-22 04:25:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a68581c1-2713-3e62-8665-b4a5d88d91d8 | -13.28998 | -45.1941 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c4c1cf7-dae7-3b7a-b839-e1d488b3e7dc | -12.22218 | -57.28451 | 2026-06-22 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea3e71ef-a17b-37a7-b0e4-acedf45d3f44 | -10.11833 | -51.66163 | 2026-06-22 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac56a481-26b2-31eb-80cc-0fd4380eccc2 | -14.14997 | -44.24495 | 2026-06-22 04:25:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66323767-b1ef-3c81-bad2-c0c792b59719 | -10.55476 | -46.2444 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87915278-c218-30b3-80d0-edbdeec1c65a | -13.84277 | -47.1254 | 2026-06-22 04:25:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4089ab89-1dce-3198-9513-36a2e182a396 | -18.24936 | -51.27728 | 2026-06-22 04:27:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f58c10e6-dbda-3988-b365-8657f260d088 | -18.25304 | -51.27797 | 2026-06-22 04:27:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb37128c-351e-3af5-bdc4-28064eb51372 | -21.66574 | -43.60126 | 2026-06-22 04:27:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 677e87d9-6cb2-330c-8f99-3ef93c3cf2a7 | -18.85527 | -47.479 | 2026-06-22 04:27:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11f06858-5d17-3541-ab74-311b996d0572 | -22.34293 | -41.785 | 2026-06-22 04:27:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d236b300-86fb-3919-8574-63785f5623e1 | -18.48934 | -51.57321 | 2026-06-22 04:27:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b83d287d-bdda-33de-9c6c-25785b536ffb | -18.25384 | -51.27343 | 2026-06-22 04:27:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8301167-589b-3026-b1b1-bcce9a5adef6 | -19.70098 | -47.32332 | 2026-06-22 04:27:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4d15e5b-e5bd-3fe4-96e6-e46c44c4a317 | -3.51643 | -48.028 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6576bf77-9ff3-34f1-b5e4-27426356b8cd | -3.51296 | -48.03377 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dc574bf-90c3-3091-865b-0eac323b7869 | -8.87536 | -46.94273 | 2026-06-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a47bdee-611a-3b31-82a1-d671d5aa2826 | -3.50993 | -48.03636 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c80b8db4-0703-3a9a-a75e-09af209956c4 | -6.25105 | -48.53046 | 2026-06-22 05:10:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0198d67-09b3-3c06-879b-af83b41c9bf2 | -8.87477 | -46.94732 | 2026-06-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16511698-c7f7-39c0-b3bb-f8124142acd5 | -3.85246 | -54.22394 | 2026-06-22 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66cff503-4a67-3364-bbef-0ad8041a939a | -3.50658 | -48.04174 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef3d82c2-70cc-396d-aa6f-33865de6e6b6 | -6.50695 | -44.70045 | 2026-06-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c2ca7578-a1ae-31ba-99a4-d33a5e3d71a5 | -3.51252 | -48.03685 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3463f662-7c3e-36b4-afe9-e30582a50de5 | -6.50766 | -44.69513 | 2026-06-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a2bae937-de98-31ba-ac52-bf2420987cb4 | -3.51551 | -48.03413 | 2026-06-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README7.md)
