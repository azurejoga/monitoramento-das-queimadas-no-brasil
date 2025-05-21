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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a14e04ce-faea-347d-ae02-b14af0cd3b58 | -13.66894 | -53.93454 | 2025-05-21 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bc6847e3-765b-3707-855c-dd46bfef14ec | -14.16114 | -45.47567 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27a38202-bf69-3f61-abeb-180fac7c6417 | -13.67226 | -53.94539 | 2025-05-21 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 166a926f-8e41-3283-99db-f93602390a22 | -24.09535 | -48.96956 | 2025-05-21 04:17:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5c22a64-d3de-39db-9bec-e84ef911587c | -12.40956 | -52.14891 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b0500ec-2a8b-3659-9924-da081e9d63e6 | -17.04897 | -46.93098 | 2025-05-21 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62fe9fce-48b6-3915-9270-939262014b1b | -12.7217 | -54.97772 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f8ae234c-9ace-328c-a8e4-1425ba11524e | -11.08055 | -54.78367 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2b09dd0f-303f-3d86-8375-2ad36e5f47a8 | -14.1705 | -45.48087 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 483fd83f-5a90-3f75-a6e0-8558a9841e89 | -11.13671 | -53.93045 | 2025-05-21 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f2e9281-3122-3111-9121-a017b48a1f62 | -15.89646 | -46.0137 | 2025-05-21 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71383764-26ac-313e-8e73-7ecf4a7e8c86 | -11.14216 | -53.93144 | 2025-05-21 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b16be7a9-99b7-3805-80d8-4a0e97b4779b | -12.36742 | -49.96957 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f69d896-606b-3131-97e2-cf41b7086204 | -12.42765 | -43.72298 | 2025-05-21 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3685750b-0ecd-3bfb-bc82-62dac81881be | -14.05967 | -53.38141 | 2025-05-21 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d092f97-5d52-3464-a0ef-6564517915a2 | -14.03185 | -55.13943 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1da23e6-016e-3f0e-afdd-410e6f10404e | -14.03802 | -50.51904 | 2025-05-21 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18536225-f3b7-3428-8e03-691e49d5b253 | -11.35594 | -55.12859 | 2025-05-21 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d6a336f-7b11-34d9-9062-d80573f20307 | -13.61158 | -55.45544 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 784e55a5-1c64-3fcd-9f27-17920710e0eb | -21.95446 | -49.92065 | 2025-05-21 04:17:00 | NOAA-21 | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 033d2369-c801-3eeb-ae31-e16dc65b4f6b | -13.19845 | -47.26582 | 2025-05-21 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dec43752-42fe-3b43-ad19-a7c872bb812f | -13.61816 | -55.45234 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4edc0fad-eae4-36a9-b8b4-ac14f9177ecd | -13.19432 | -47.26908 | 2025-05-21 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df870d46-aaba-3462-a3cb-9eed607d675d | -17.70908 | -47.49323 | 2025-05-21 04:17:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf6bd0d8-43ab-3443-931d-9bd304ad7732 | -20.95753 | -56.60057 | 2025-05-21 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2e9d93c7-1d2d-3692-a6a9-55ba16c7602f | -14.68849 | -45.10846 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12810d93-2a2c-3747-95ef-0d6332c27d04 | -20.95599 | -56.60769 | 2025-05-21 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44badad5-3d81-3c98-8c76-ced6ae51ba06 | -14.03108 | -55.14326 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32d31911-c048-31e4-95a6-905ee2180f31 | -21.60402 | -52.38512 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d1f3806-c196-3f71-a52e-6e5570eeb262 | -23.34089 | -46.77149 | 2025-05-21 04:17:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e117894-750c-348d-ac55-a495e8c71917 | -11.29357 | -53.97756 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8fdaf0a2-4480-3fab-8ddc-008babc559c3 | -15.09958 | -52.83581 | 2025-05-21 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6816f9a5-230e-3557-b762-dd751ab56d48 | -12.35853 | -49.97185 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f8c494f-ea0d-30dc-b5fb-3d5ce43729e7 | -17.2395 | -48.2426 | 2025-05-21 04:17:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 539e04b3-9470-3982-ac74-c3d25e839f81 | -20.94985 | -56.61002 | 2025-05-21 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 64266f24-afaf-3d70-82fb-f5a2e48e094b | -20.2218 | -50.76077 | 2025-05-21 04:19:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 71c92d3e-2b9b-3b27-82e1-641f7718f5af | -21.46046 | -47.36852 | 2025-05-21 04:19:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8feea10-ac29-35c2-8fa4-df5fa46ee8df | -21.59593 | -48.49197 | 2025-05-21 04:19:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91e3f697-62d0-36e4-ba5c-c5d2dfca11c9 | -21.62685 | -43.46651 | 2025-05-21 04:19:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b57c9325-2a2b-322e-9928-4ca550648e57 | -21.25443 | -48.49302 | 2025-05-21 04:19:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0eeb3473-c09d-3ebd-8f31-60df8433586f | -20.51654 | -44.17972 | 2025-05-21 04:19:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2aaf67f5-2fe3-3094-8e3e-a594899a610c | -21.04308 | -43.20269 | 2025-05-21 04:19:00 | NOAA-21 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 367ce638-c9e4-3bf7-8a77-73ce04bd4bd5 | -19.81143 | -54.41484 | 2025-05-21 04:19:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 621ac9f1-e533-317f-9711-0cab70d2b450 | -21.45655 | -47.37164 | 2025-05-21 04:19:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 433b99dd-1661-304f-ba24-3cf37fa9e7c4 | -19.11338 | -52.69768 | 2025-05-21 04:19:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a9f8800-131f-304c-91ec-659dd5d585d0 | -20.31065 | -45.58255 | 2025-05-21 04:19:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0647d4a5-c78d-38bb-ae8e-1d1df31ef7cb | -21.26409 | -43.47743 | 2025-05-21 04:19:00 | NOAA-21 | SANTA BÁRBARA DO TUGÚRIO | MINAS GERAIS | Brasil | 3157302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fe6c88c5-cf9b-3952-b303-6f5d6d160560 | -20.41671 | -43.5518 | 2025-05-21 04:19:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ef49008c-378d-34aa-8756-35337d6605c0 | -20.06154 | -43.74093 | 2025-05-21 04:19:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e55199f2-3542-3369-bf1b-343bfcc0d685 | -18.90661 | -53.03394 | 2025-05-21 04:19:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9c0a907-dc5f-3fce-8dfd-c99edeb34ba3 | -19.06083 | -53.454 | 2025-05-21 04:19:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7273f50-e4e7-3c5a-873f-6568f515284d | -21.1089 | -48.07982 | 2025-05-21 04:19:00 | NOAA-21 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44b47e8c-6e7b-3fbf-8f04-95b700bcc2ec | -19.97398 | -47.18948 | 2025-05-21 04:19:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ee5dd0e-4f07-3818-8f65-2995a4b63d0e | -19.74183 | -54.51159 | 2025-05-21 04:19:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97085f9b-d3f7-342d-b1ac-9ba94cb071cd | -19.05526 | -53.45812 | 2025-05-21 04:19:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58bada7c-6692-3eda-85ee-a2bdd9462d83 | -27.6043 | -50.17295 | 2025-05-21 04:19:00 | NOAA-21 | PALMEIRA | SANTA CATARINA | Brasil | 4212056 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4211436c-7285-37ba-a783-897ff722a702 | -19.97731 | -47.19005 | 2025-05-21 04:19:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 788e2bfd-e2a0-3e28-bef5-ee356972479b | -25.56796 | -49.36831 | 2025-05-21 04:19:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b7786e6c-bc64-3f82-96d9-e89dd2ddaa10 | -21.22014 | -48.61245 | 2025-05-21 04:19:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99571378-964e-36a8-afb3-78a0c1f38bd3 | -21.46378 | -47.36911 | 2025-05-21 04:19:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 78a38434-5133-360e-a918-2cba4dfb18ce | -20.22271 | -50.75578 | 2025-05-21 04:19:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d21ed582-a046-393e-9d9f-921c9d2f01c4 | -20.19269 | -48.0201 | 2025-05-21 04:19:00 | NOAA-21 | MIGUELÓPOLIS | SÃO PAULO | Brasil | 3529708 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e90eaf1d-a0e5-345d-aeeb-f4b2abb9bf5a | -20.31341 | -45.58683 | 2025-05-21 04:19:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9595f8a6-530f-3e47-8a0a-badc6eaffc9e | -19.05982 | -53.45909 | 2025-05-21 04:19:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76c850ba-5249-3c55-b7fb-6e4d75336851 | -19.73585 | -54.51622 | 2025-05-21 04:19:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08fe5d4f-fbe3-32d6-a8be-bda8e0143de4 | -21.93943 | -46.31247 | 2025-05-21 04:19:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5f391ab9-6ef8-30bd-ba90-1256df9645d5 | -19.73704 | -54.51041 | 2025-05-21 04:19:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a5b02c4e-d874-3d42-8142-d438195aa414 | -21.46318 | -47.37284 | 2025-05-21 04:19:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d13d51a9-2d36-3ffd-b252-f4ba5a317867 | -20.36121 | -47.42674 | 2025-05-21 04:19:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c68537e5-0a71-3c40-927e-43c6e7faa973 | -19.969 | -44.21708 | 2025-05-21 04:19:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ae4025f-9673-3f50-9ee3-63a66b57db0c | -21.45987 | -47.37223 | 2025-05-21 04:19:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c155ab3-3cc3-3a09-bebd-55a4bf9823cc | -21.12133 | -48.67555 | 2025-05-21 04:19:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e1156b47-0e08-3be7-8c5e-3dc5e1a536f6 | -19.66528 | -51.33983 | 2025-05-21 04:19:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fb87a00-f848-3fc4-8641-82fb83b50f69 | -19.8266 | -54.58152 | 2025-05-21 04:19:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81961182-ee6a-3475-895d-1fa66c948198 | -21.45715 | -47.36792 | 2025-05-21 04:19:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 67e10754-32ed-3bb3-a3e9-780efd243e59 | -20.361 | -49.30682 | 2025-05-21 04:19:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2bd20290-cc45-3ce1-a883-9c5fb9018cd0 | -19.11687 | -52.70299 | 2025-05-21 04:19:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4124e592-35a1-3482-bd7a-f14d2c200aa9 | -20.59748 | -42.12871 | 2025-05-21 04:19:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7924b7f4-88cb-3273-a7b7-5d5a1434f71b | -11.0903 | -54.7648 | 2025-05-21 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| f7fc1339-8224-3cdb-bddc-a65722def20e | -11.0712 | -54.7868 | 2025-05-21 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| aacbe88b-7295-3ad6-831b-5c00d0bb15d8 | -12.2946 | -52.4785 | 2025-05-21 04:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2cda2d87-1938-3215-8095-3b8ef02a4c58 | -11.0901 | -54.7852 | 2025-05-21 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ad3604ab-1d12-30f4-8e62-833beaaf0017 | -11.0714 | -54.7664 | 2025-05-21 04:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| aa00933f-a2ed-346e-900e-259a63530649 | -11.0712 | -54.7868 | 2025-05-21 04:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 3529a099-b50f-39c1-9e68-6568e240ed1a | -12.2946 | -52.4785 | 2025-05-21 04:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 79e92366-9788-39ac-9bc9-9ddfa6b9a801 | -11.0714 | -54.7664 | 2025-05-21 04:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 22687ddb-d43d-31d6-a406-98363bb7afb2 | -11.0712 | -54.7868 | 2025-05-21 04:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 28cdca72-16cd-3499-aad5-5d5bb227f868 | -12.2946 | -52.4785 | 2025-05-21 04:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 71289415-c591-3a18-8468-e5034414d24f | -5.44191 | -46.29001 | 2025-05-21 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e4e7a6d-5f4c-34cc-bb23-8328eb99afd8 | -10.10848 | -47.12719 | 2025-05-21 04:40:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7b95ef4-b112-37a9-951b-b273eebba47c | -10.12187 | -47.11192 | 2025-05-21 04:40:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e6d18fb-142b-37a4-b090-6e5a98c40128 | -6.46643 | -47.39811 | 2025-05-21 04:40:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33cd7903-5587-3643-8600-43c64582d827 | -6.63215 | -55.01181 | 2025-05-21 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cb55b0a-3964-308c-ac53-227dcfcb62aa | -9.57389 | -49.1086 | 2025-05-21 04:40:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2b2a734-3709-317e-a1d7-9c4fcc6361fb | -10.1091 | -47.12295 | 2025-05-21 04:40:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 904377d8-1b4c-3dcc-bbad-b68df2cf0ec6 | -9.57492 | -49.10833 | 2025-05-21 04:40:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a54a85e9-7b28-364e-99d0-af79218a04ef | -9.25431 | -44.4848 | 2025-05-21 04:40:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58510f46-46f2-3d08-b8b4-46a1b19a0a15 | -4.23484 | -48.97409 | 2025-05-21 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65f186d6-f187-31d1-bbe0-55bf7bf65f46 | -8.04752 | -49.65686 | 2025-05-21 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf94f65d-6730-3ec4-88b5-97e8b03964e3 | -8.74616 | -49.74935 | 2025-05-21 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
