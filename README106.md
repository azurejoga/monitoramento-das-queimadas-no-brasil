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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77aa79a7-3b9e-3626-83f5-8de7f5aa529e | -11.6967 | -54.6081 | 2026-09-01 15:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 90e6adc9-ec4a-3561-a29c-9a6f9e01a00e | -13.0897 | -45.163 | 2026-09-01 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 20fe23b8-47a7-348d-b36d-cf863370d019 | -7.2934 | -60.5713 | 2026-09-01 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| aa1578cc-5b2c-3aa6-b4ed-be48fc7ccde7 | -6.8009 | -59.5742 | 2026-09-01 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0dc6c674-f1ea-3024-9d56-3d1cb9b25ffb | -11.2295 | -51.2667 | 2026-09-01 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| ac7381de-f77d-396c-ba4c-57400f8a7fea | -8.163 | -55.4266 | 2026-09-01 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3fa3b4e6-fcad-31da-80c5-5bad7b58a747 | -9.7028 | -48.1366 | 2026-09-01 15:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3788190d-1aac-3f91-830c-e14b02148a0c | -10.3574 | -50.0171 | 2026-09-01 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 4d998910-3963-3cb8-abf9-fa444b031bfb | -8.9242 | -63.2804 | 2026-09-01 15:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| b975a39e-0ccf-3de8-82b3-d49c64054a3a | -7.5709 | -60.4835 | 2026-09-01 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.3 |
| da4d5da6-a362-3c5b-a91c-2e1ff69e671b | -11.0437 | -49.6635 | 2026-09-01 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| f8dae6e8-e2b2-3039-8092-5aebf5b55d61 | -6.0981 | -53.7916 | 2026-09-01 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9b6dcaec-3359-3a5c-9fc7-f6f100006c3b | -10.0105 | -46.4161 | 2026-09-01 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e4a2a330-4922-3d90-ae8a-f9e0db10932e | -11.0434 | -49.6851 | 2026-09-01 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| c51a6d60-3c24-356d-8f85-91821ca1e3d5 | -10.3577 | -49.9957 | 2026-09-01 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 222.7 |
| e957c48b-8ad8-34fd-aead-24ff7078a65b | -10.8206 | -50.7159 | 2026-09-01 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| eeb87906-a201-3b8a-b28c-8c34e28ba9b1 | -8.5977 | -54.6948 | 2026-09-01 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| acaf04cc-fbd7-3e06-9b62-416429f36056 | -5.5832 | -60.2116 | 2026-09-01 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 89aa91e7-c6da-38b1-b29d-d91732bc23e9 | -5.9451 | -57.6906 | 2026-09-01 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 2f39970f-64ad-3351-a774-04ca3a65ed02 | -7.4549 | -61.4044 | 2026-09-01 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c69b3cd0-e516-379d-88c3-ed7d60327746 | -13.4325 | -57.061 | 2026-09-01 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 91ad84c7-dbe8-32bc-aac9-2137035cb34a | -5.9635 | -57.6899 | 2026-09-01 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 84362e01-81bc-386a-91f7-9e8d04ca76fb | -13.3946 | -51.7382 | 2026-09-01 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 41052bea-904d-38aa-aa4e-240e8bcd2e3c | -13.3943 | -51.7595 | 2026-09-01 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c4cc3b14-47de-36d5-85fc-0c059433e67f | -14.6535 | -53.5642 | 2026-09-01 15:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 6718ec3c-b1be-3a45-92b4-dbc5b03ac354 | -15.6475 | -50.1062 | 2026-09-01 15:10:00 | GOES-19 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 02d45f84-296a-3084-989e-8bd0dbd5cf04 | -11.7216 | -47.6327 | 2026-09-01 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| c7827560-5440-38c1-8a37-512fcf040429 | -1.4394 | -54.2169 | 2026-09-01 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 7657b631-2abf-356f-a419-b0273623ecdb | -10.2212 | -50.3303 | 2026-09-01 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| ad0eab9c-e975-3942-b8a3-eb69166ee4f5 | -9.4606 | -67.4531 | 2026-09-01 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 05533dca-e33f-32a5-a827-f3e9c626e030 | -11.6975 | -54.5467 | 2026-09-01 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b487985a-9976-3efd-925b-f25899489c1f | -10.3394 | -49.9547 | 2026-09-01 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d7790c75-16d6-3d80-9399-1fa98b67274a | -4.1515 | -60.7068 | 2026-09-01 15:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 42090bc1-51f7-34ad-83f9-719754414c80 | -14.7302 | -53.5966 | 2026-09-01 15:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 65e80573-6e83-3f90-8d8e-56075f56557d | -14.5025 | -52.2126 | 2026-09-01 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 09e1bbac-c855-39b0-b3c3-81e8b647aaee | -3.4979 | -59.0409 | 2026-09-01 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e5839b9b-8327-3b3f-9bc5-165935a11464 | -5.5833 | -60.1924 | 2026-09-01 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| d2cd3dba-5d5a-3002-a840-65c3dfe466b7 | -10.7856 | -50.5066 | 2026-09-01 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 89bcb7f3-78f0-3ced-8584-624d1f7cfc9e | -15.4202 | -41.2232 | 2026-09-01 15:10:00 | GOES-19 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 110.4 |
| 98bc055b-95ad-38f3-a63f-f0159fe31b6f | -12.9032 | -45.8382 | 2026-09-01 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 292.2 |
| 79eb5b45-b147-3e88-adf4-fecd603c1842 | -3.1266 | -61.2188 | 2026-09-01 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cb53e5fc-99ff-3bba-8e64-b38f5da736a3 | -13.3936 | -51.802 | 2026-09-01 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 49b7f992-ac25-3528-a6cb-642a0af00084 | -3.6216 | -60.547 | 2026-09-01 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 077b0bd5-cb39-3490-b029-e1b07273ff43 | -17.91 | -50.47 | 2026-09-01 15:15:00 | MSG-03 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e7d3737d-580b-3409-9a9f-141089af5801 | -16.84 | -48.54 | 2026-09-01 15:15:00 | MSG-03 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c7242ca4-2082-384a-814d-c177fcaddce2 | -10.37 | -50.02 | 2026-09-01 15:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32fe322b-f031-3328-9b82-85d398cee00d | -12.9 | -45.79 | 2026-09-01 15:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e73691b-c4ef-3994-8b55-ff3ac53c4bb9 | -10.72 | -46.26 | 2026-09-01 15:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8d9288b-d418-3e07-b204-3c766bbb182b | -6.09 | -43.72 | 2026-09-01 15:15:00 | MSG-03 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 743e75cf-3a01-3e7c-8a95-700ff9eaa660 | -10.02 | -46.48 | 2026-09-01 15:15:00 | MSG-03 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b7c3af7-7028-3391-ae4b-bab338b8ba5a | -16.87 | -48.61 | 2026-09-01 15:15:00 | MSG-03 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c710d68d-96f5-3de8-ae4d-853a968bc6d1 | -12.9 | -45.84 | 2026-09-01 15:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5eff23a-86cc-3261-bc50-f12e1659dcef | -16.87 | -48.55 | 2026-09-01 15:15:00 | MSG-03 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09b094cd-bdf7-38a7-8823-f6419a0e3c2d | -3.87 | -44.02 | 2026-09-01 15:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dadd542-a3fd-3332-ad80-8b13f2ab28b5 | -16.84 | -48.59 | 2026-09-01 15:15:00 | MSG-03 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be01973c-6f70-3d79-858f-ba65c6e457df | -11.56 | -45.47 | 2026-09-01 15:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 958c9168-d62c-3dea-879f-6ad2ba815615 | -3.87 | -44.07 | 2026-09-01 15:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1556bc6-6a4e-385d-88f5-827a14e0488a | -6.09 | -43.67 | 2026-09-01 15:15:00 | MSG-03 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97491ec5-beb7-3a2a-a01e-204909d8237f | -17.91 | -50.41 | 2026-09-01 15:15:00 | MSG-03 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 66c855ca-b1ee-30ae-adc8-9648989390fb | -10.87 | -45.34 | 2026-09-01 15:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2657e64-e2d2-3e03-8e59-c8204f3142c1 | -10.88 | -45.39 | 2026-09-01 15:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34073d2c-cc5d-31bf-bae9-c6d8940666c6 | -10.7856 | -50.5066 | 2026-09-01 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6fc3b898-6d00-3454-99a5-7a7c97f1d2e8 | -7.5846 | -61.3232 | 2026-09-01 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| aa578b1a-8423-3c3d-95d0-a4a8e9d25f98 | -11.2478 | -45.1425 | 2026-09-01 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 246.4 |
| d921fccf-2eee-3a0e-ae95-e9dfeb0da898 | -10.3577 | -49.9957 | 2026-09-01 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 341.0 |
| e896b853-7b9f-3116-a709-79d91843fcac | -13.471 | -57.0373 | 2026-09-01 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 239.5 |
| b8a32e19-1560-3953-907f-b32f9bb9b946 | -13.9477 | -54.3971 | 2026-09-01 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 241.6 |
| 032d2fd2-6973-394c-866b-5b0305ea35ef | -13.4325 | -57.061 | 2026-09-01 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 9a78b2fc-dc53-3b72-9773-cd37f5c0b75b | -10.0105 | -46.4161 | 2026-09-01 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| efda7789-da32-3d23-bc29-f3aa6140dd7a | -8.6152 | -54.8146 | 2026-09-01 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6a22f89b-f74c-33dc-b173-948e6b9314aa | -3.1998 | -61.161 | 2026-09-01 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| f9ab0ea8-1a81-3dcd-859d-debd5eb4a56a | -6.369 | -54.7655 | 2026-09-01 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 9f0d8eab-fcfc-39b7-84d9-a87853036d13 | -11.0434 | -49.6851 | 2026-09-01 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| bf5212c7-3c73-3322-982d-2cee90ea658f | -11.269 | -54.0334 | 2026-09-01 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 966997fb-da02-338a-8008-6463664f3a24 | -3.79 | -59.3031 | 2026-09-01 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 0b45c157-249b-3b8f-9c37-a97811eb4132 | -13.967 | -54.395 | 2026-09-01 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 571.7 |
| b4508762-4fb8-3cde-a45d-762c0a876a0b | -5.5649 | -60.193 | 2026-09-01 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.0 |
| c70a2280-4770-3817-83dd-5553ec2766e0 | -4.181 | -63.1543 | 2026-09-01 15:20:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 172.8 |
| df0cdd2b-3c73-3504-ae00-6b8bff5f6d59 | -6.8009 | -59.5742 | 2026-09-01 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 168438b1-1dee-3713-ac16-3c997a86b818 | -13.4516 | -57.0592 | 2026-09-01 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 306.8 |
| 4f2f7b6c-ef06-3bdc-a9d6-ea204cea194a | -7.5709 | -60.4835 | 2026-09-01 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 9573ce56-0dbf-33ad-be4d-aea21130fd9e | -9.4606 | -67.4531 | 2026-09-01 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| dbb95d67-24ab-3307-889c-3db93e42b842 | -7.98 | -44.2731 | 2026-09-01 15:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 3716a7b8-eeb8-3daa-b407-d4fea0ff101c | -11.2767 | -50.6029 | 2026-09-01 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 39f291a5-2eaf-3d76-8dd3-8dfe40304996 | -10.7593 | -54.0589 | 2026-09-01 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4adeb9b3-5484-3477-b2e5-b02868dd33fd | -10.7407 | -54.0401 | 2026-09-01 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 171c435b-c780-39e7-bb55-19be18a3e779 | -3.1267 | -61.1811 | 2026-09-01 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 876d1c73-ea44-3867-a4c7-a05eb08c6bbc | -11.0623 | -49.6829 | 2026-09-01 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| c3689f33-47ba-32cb-8698-51d2b2aa0bf7 | -12.1457 | -44.196 | 2026-09-01 15:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 7e642f8f-f48b-34f8-989c-f92e6d287e61 | -8.9242 | -63.2804 | 2026-09-01 15:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ed1ab0ea-82e4-33e7-aa03-5be91f376016 | -10.2212 | -50.3303 | 2026-09-01 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 5c4d7aff-42c5-3889-b165-94f661d214bb | -11.2298 | -51.2456 | 2026-09-01 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 353d980c-f334-3b2f-a026-d4973f59cfca | -15.4429 | -52.681 | 2026-09-01 15:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 77e487fe-d137-36bb-8d8b-101e3d5496c1 | -7.5661 | -61.3239 | 2026-09-01 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| fbb58dfd-bb29-3c99-85dd-ab62786e338c | -3.5162 | -59.0405 | 2026-09-01 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f5044f0b-6e49-3207-bfd1-4e5a741e679d | -14.5627 | -52.077 | 2026-09-01 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 26c77c34-b314-329d-a777-0e33ec21382f | -3.6216 | -60.547 | 2026-09-01 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 76bd234b-1849-3604-be9f-237e1a995bdb | -3.1083 | -61.2191 | 2026-09-01 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8aedb014-4151-37e8-8048-2eaeb43a7cd3 | -6.9514 | -59.0666 | 2026-09-01 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 34908bce-3d4b-302f-8639-5270dddd2abb | -7.571 | -60.4643 | 2026-09-01 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.8 |


[Clique aqui para ver as próximas entradas](README107.md)
