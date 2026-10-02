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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27c851b9-b051-3b19-89ca-8f5f3231815c | -3.03368 | -53.87875 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1023c70-b5ff-3684-8e1f-8e49368dd097 | -8.97549 | -48.94123 | 2026-10-02 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52e69330-846a-3a41-94fe-0815873659a7 | -4.26898 | -50.78012 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30b2e116-788f-3d11-a370-d692d66c56a9 | -6.89943 | -43.68768 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02323ef9-7420-3488-91a3-f412d45ae229 | -5.75677 | -45.15835 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c2f4a38-a85c-3446-8cf6-53bb85863976 | -7.74981 | -54.81261 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97207b7e-956a-3f1f-848c-7b25dcaf3677 | -6.09054 | -47.67127 | 2026-10-02 04:14:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e325bfe-f103-3d20-bf02-59e0c2406471 | -9.83767 | -44.83434 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 688eb350-6db7-3aed-9666-fa18e66233fa | -3.17792 | -54.10277 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3e9a000-512c-34ca-b702-cf76741c6d03 | -8.38546 | -46.29034 | 2026-10-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34f464ad-f435-3f0e-a2a3-4154ddcc9437 | -6.23995 | -53.13834 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b6860a9-c281-34bc-9a25-e8f49f3d0738 | -3.29115 | -53.86398 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9ef9b7a5-750d-3cfd-822a-31947a18aff1 | -4.26785 | -46.53509 | 2026-10-02 04:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ff34d93-e19d-3c0a-9598-d86a8c4b87ce | -4.25925 | -50.77121 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb1b8e95-fef1-3b1d-befd-6230916edf48 | -6.16932 | -44.59006 | 2026-10-02 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf27beba-fbda-36ff-b2b8-f3e5a806c478 | -6.19545 | -44.27755 | 2026-10-02 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfda7102-6bed-38c4-a576-2a801e82fcf8 | -4.26841 | -50.7508 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b9859b4-6464-3c1e-b29b-ac5d9b0d5e5d | -6.74976 | -55.0913 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c251785c-5d42-3f82-91e7-ec3c217744f3 | -3.12638 | -53.7459 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a78ea9b7-5893-3554-a870-1d2fe9493f5b | -4.26539 | -50.76828 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bad5b6ed-954b-30ba-a01c-e2a39a25dc10 | -2.25061 | -48.75057 | 2026-10-02 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4e1b39c-f5fd-3128-90b2-ea28288b91c8 | -6.01079 | -44.25349 | 2026-10-02 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49ea92fa-b438-3839-a93e-7ec1913f130d | -4.03387 | -54.24438 | 2026-10-02 04:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1ebb1f0-7a09-3301-b1f5-74a3910bb560 | -8.75713 | -35.11692 | 2026-10-02 04:14:00 | NOAA-20 | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 20f35a75-7b79-362c-bbb2-41f136341fe1 | -9.81595 | -44.81478 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 524a9509-4161-3475-8adb-eeead202016e | -6.8317 | -40.87072 | 2026-10-02 04:14:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 38e9de3b-0394-3993-82b3-00a43d817cbb | -3.06308 | -49.3699 | 2026-10-02 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 658f4d94-999f-3e59-978e-4e4dd28cecdf | -6.34328 | -43.37704 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da68f5c9-ff85-3c34-858e-bdbfda1f6fb8 | -4.25751 | -50.74876 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d0ab2ea8-31e1-3fff-a858-e9b8ce90c310 | -6.0848 | -47.67894 | 2026-10-02 04:14:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de0408b2-9db3-312f-a96d-a215e162a699 | -9.13409 | -46.66486 | 2026-10-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa63b6e6-7ad2-33ec-baeb-318bc1628eab | -7.19418 | -46.55107 | 2026-10-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4c3682d-d040-3837-b4a3-d1633accf5f0 | -4.05594 | -51.12251 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72cae4a3-59a6-3bd7-99d3-a330db2cb8d9 | -3.15955 | -54.08677 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c54fed0-b17f-33f3-a50b-f937b4f29df7 | -9.12343 | -44.74307 | 2026-10-02 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acf5aecb-2dd7-3864-89a2-fa95bfef41ee | -7.83815 | -55.13933 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52cbff22-5057-3259-bd31-6524fd2a9eaa | -4.27196 | -46.53571 | 2026-10-02 04:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5c8d58d-8133-32c2-b031-28e6753f6a09 | -8.00345 | -42.90889 | 2026-10-02 04:14:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cf077ce5-1010-31b4-9c74-aea6107a2d8d | -3.00925 | -53.88774 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| af3bd359-4e75-333f-ab97-8668846f353a | -3.29221 | -53.85796 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e4a779e-4899-360c-bd36-fcedf7900fff | -3.29432 | -53.84592 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 97ebfadb-ff34-3a7b-9c9c-80c2a4f5929b | -6.33065 | -43.36369 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| acd348df-5cab-3ce0-89e6-6fdbf36fa985 | -4.27091 | -50.76893 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f4a4ab6-1232-32a5-85bc-e1f5a7c4d3e5 | -3.28652 | -53.85081 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 0a0a4f8c-2a77-3a97-ae04-531b1f1037ea | -3.17111 | -54.10136 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 60a19b62-e306-33c9-91a3-83321d93937c | -7.71436 | -54.81768 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8de1285a-ec5d-3a26-a95f-46a134eb136a | -6.20502 | -53.26018 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 424092dc-3f76-3837-a6d6-39a0e1feaedc | -7.57456 | -55.13472 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c97976bc-958b-374d-a8be-16efd4ebc7b6 | -5.99769 | -53.54576 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c829371-7b71-32cc-a9e6-364246b554b6 | -7.20596 | -46.55311 | 2026-10-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f410060a-a1f6-367d-a092-3365df1fa92d | -5.14007 | -49.87464 | 2026-10-02 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2866c27-5347-3c4c-8f39-07a52fea762b | -6.44913 | -43.82673 | 2026-10-02 04:14:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab2fe236-c023-3f21-8ced-2640f740ddd4 | -9.83831 | -44.83047 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d56a40bc-84f6-3443-81e4-ba514a0ded71 | -7.73876 | -54.79833 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d65e7892-b3b4-31e0-a8a2-2549979d5e45 | -6.90003 | -43.68396 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ad48f98-bb97-3d9a-968f-c3b0b4bb83fa | -9.75788 | -44.80954 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddee0f00-c58a-3342-91ea-c71b5ae788e6 | -8.02799 | -47.47786 | 2026-10-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5302048-546e-3d41-9f63-aebdebbcf6ba | -9.20793 | -45.79665 | 2026-10-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33ab24e5-3fa2-3864-9501-7f6cc8dbee08 | -5.55387 | -37.32147 | 2026-10-02 04:14:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8ba36b32-91c0-3ce2-8076-f27dee1434f3 | -5.7411 | -43.28161 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5efba5f-6a83-3889-8f6d-35d9ee0c97e1 | -4.30126 | -50.78922 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 09981e3b-0e1b-3b32-bdb6-c2888029399c | -7.83388 | -55.12529 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9452aa7-155a-3b07-9dc7-52864edd49a9 | -8.01451 | -42.92514 | 2026-10-02 04:14:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ee3c3bf2-affd-366a-ad0c-9c4f190f7865 | -5.11025 | -37.4449 | 2026-10-02 04:14:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b76d443f-661b-3fc8-bb5f-8af2582875c8 | -9.52311 | -45.32916 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a867897-3c9a-3e73-98be-3aa7e88aa816 | -7.51752 | -47.33854 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84c75d19-1c0f-3744-a57f-986eebde61f0 | -6.91087 | -43.68192 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b630ec61-59bc-3447-90ce-971281c85fd3 | -5.74508 | -43.27851 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fe6460e-471f-3746-b4bd-f828977583e9 | -3.28546 | -53.85682 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 295c9ab2-b5e6-3bdf-b0ee-d40dfd1921f4 | -6.96236 | -42.84934 | 2026-10-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4da8d80f-9eee-3d4c-a5ce-a8eab1846f5b | -3.04042 | -53.88005 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d636539-b38f-368f-b3de-83850ad2b563 | -3.27231 | -50.08856 | 2026-10-02 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 411cac9c-91b7-32f0-a082-6274c42458ff | -7.83015 | -55.14429 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2377f871-9c49-3d45-99d1-09ecf11656fd | -9.80617 | -44.8092 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa819cc3-740b-3b32-810b-eda0d38c5326 | -9.82532 | -44.84426 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8209567b-c4e6-3e1e-b4be-6d7e3d1eeec1 | -8.414 | -47.63603 | 2026-10-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01fee742-c500-327a-be19-c53f54cdd2c7 | -6.2355 | -53.12779 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df6367c5-f217-367a-ac6f-172d73f83408 | -7.87215 | -44.17645 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2592c6b6-d1e2-3c39-8306-0d5a6ce8a0e5 | -6.07571 | -53.31006 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13f2e3a8-b1cc-3778-9bb3-6d021d5bd30b | -5.23111 | -49.57816 | 2026-10-02 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65196bd6-97d8-3086-8d36-376a5f482e71 | -6.8707 | -55.56726 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9dd069f6-82dd-380d-890b-1afbdf6ebea2 | -4.05859 | -51.12206 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1222c04f-d9a3-3cfa-ad28-7c9eddfb676e | -1.99762 | -49.66739 | 2026-10-02 04:14:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9bfd7d3-9dc4-303b-a566-98f12804f72f | -5.69417 | -47.1671 | 2026-10-02 04:14:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4778a883-c294-3c37-92b3-8f5a984f48a7 | -8.08087 | -54.88799 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f71da00-31fc-3220-b22e-055d71bff22d | -6.24081 | -53.13362 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e80d124d-02af-33c0-9995-4affdc1e82c9 | -6.24369 | -53.15287 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5647e042-fa2e-3e2c-a49b-86774b2314c9 | -5.89214 | -53.5002 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4137cb5a-6e6f-3fb3-add3-d71561b3bdf3 | -5.89917 | -53.49749 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| db815c42-c1c7-394c-aebe-deafad3008e4 | -3.06663 | -49.36817 | 2026-10-02 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81484832-a48d-36ec-bd11-4c8aebb00b47 | -4.27149 | -50.76556 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4826837-20c8-313b-80db-4f4f8449dd2a | -2.89413 | -54.14475 | 2026-10-02 04:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5aa75f90-39bd-3973-a6a4-d2ca36039648 | -4.06478 | -51.11961 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4cafcf1-ed92-35bb-b31d-6e2f490229ce | -6.34168 | -43.36547 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3077403a-46d7-30d6-8eee-86560b762bb1 | -3.13205 | -53.75306 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 64e7efe6-dddf-361d-9d87-78e1a9e56792 | -6.8902 | -43.70141 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 545a4d42-a334-3cd0-a983-4f99defa27e8 | -1.99815 | -49.66419 | 2026-10-02 04:14:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3199a04-ceaf-35ca-9cb2-fa32bd9c1944 | -7.52799 | -50.52991 | 2026-10-02 04:14:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 477202e6-b3f9-397f-ab58-468af0c961d6 | -7.8709 | -44.18406 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 313bd0fc-9a3f-30c0-9f54-3cf7c15a7c00 | -7.41302 | -55.59896 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README38.md)
