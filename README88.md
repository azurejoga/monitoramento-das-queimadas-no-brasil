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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f6d7620-d570-36de-988c-6bd366ccea1d | -20.35068 | -43.885 | 2024-10-04 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a1027aef-dee0-367b-b021-4054fb6551e7 | -20.34023 | -43.86406 | 2024-10-04 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3ae13be6-732a-38cf-9662-8912bfb1ecad | -20.27866 | -44.11124 | 2024-10-04 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d99043a2-9abf-3a5d-9a95-0097850be371 | -20.42993 | -43.76429 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 14fa2718-e6f2-3bda-888b-9b4a0f3721aa | -20.4288 | -43.77172 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3ffc755f-d3a0-3d5d-96f0-9ef218552837 | -20.42326 | -43.7632 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 81395f02-d085-335c-a0f5-bd8b55f2b37e | -20.41825 | -43.77368 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 87c18da8-006c-3fd3-acd0-3c7b52370cc2 | -20.14036 | -43.83801 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 142b289f-cf85-3f73-b259-16aeba9228eb | -20.13146 | -43.85167 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1798d8df-549b-3abf-9470-340eba999f64 | -20.01689 | -44.50668 | 2024-10-04 04:12:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eae0cfe6-f865-3aa5-a5d6-364785a4320a | -20.01472 | -44.49879 | 2024-10-04 04:12:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 903aa356-84ca-3f20-a3a0-8d8970a02113 | -20.00868 | -44.49399 | 2024-10-04 04:12:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0374c50d-c68e-3222-ad5c-0c6599422b46 | -20.00538 | -44.49341 | 2024-10-04 04:12:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 27b0bfbe-be71-317a-9e35-6d35a203fb5a | -19.96097 | -44.27582 | 2024-10-04 04:12:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3334d321-c6a8-384d-a4c0-d1c56b5f5f2e | -19.91927 | -43.83916 | 2024-10-04 04:12:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a0ff57e2-efc8-38d8-83f7-4ff5496ee802 | -19.8926 | -44.51912 | 2024-10-04 04:12:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b96b03b4-be67-3d72-adfa-c7d82aea969b | -19.86944 | -44.40636 | 2024-10-04 04:12:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ffd894e1-4ca4-3f6e-84e9-e4317515000d | -19.83508 | -44.23205 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db713ba5-d66d-3d3a-9a70-19cf59cd331d | -19.77983 | -43.90663 | 2024-10-04 04:12:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4df965ae-8d19-3a4b-9dff-4c083c5cb494 | -19.75808 | -43.69099 | 2024-10-04 04:12:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0887c8b2-05b2-3dc9-82dd-bfc681718720 | -19.75699 | -44.27522 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 646411e8-efb8-31cb-99d4-05bac76ecd69 | -19.75369 | -44.27465 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 835db327-6702-36df-af33-f44b748ab66b | -20.21061 | -44.7468 | 2024-10-04 04:12:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecb16af8-7d2c-3374-994a-8a06fa1bdea5 | -20.10643 | -44.91245 | 2024-10-04 04:12:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3576223c-e68d-3fea-9b75-2e3bc593daa4 | -19.88175 | -44.14988 | 2024-10-04 04:12:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3295b0c6-8011-3bb4-aee9-fe5b260bf3d0 | -19.8417 | -44.23318 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 09993700-4e82-3b03-94b1-644e119d6a2b | -19.83565 | -44.2284 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29e40532-2f9f-3998-b888-fa604fa4a57d | -19.81506 | -43.76517 | 2024-10-04 04:12:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d170d03-eec3-38f8-a7d1-d24e04965a17 | -19.8064 | -43.64248 | 2024-10-04 04:12:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b68a2159-1dd4-3348-9fc5-f0b56ea71de9 | -19.79973 | -43.64137 | 2024-10-04 04:12:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baf771ff-38ea-36ce-a52e-9ff2411fbaf8 | -19.75756 | -44.27158 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cc59498-2350-3c4d-b9be-7f3dd531b291 | -19.74651 | -44.27716 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b55ff71-dcc3-32b1-bb35-c526471cbb9a | -20.18562 | -43.76176 | 2024-10-04 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1a1a832c-cc00-369f-92f0-c3e5f932ccac | -20.15701 | -43.5475 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 547043c5-c516-348f-b0cc-90f5c8b86eb7 | -20.15644 | -43.55127 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 88547458-edd9-32bc-bf29-49c5bd5dc048 | -20.13973 | -43.86449 | 2024-10-04 04:12:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8d4a0c13-fff6-345d-80ef-10a2856bcf42 | -20.13478 | -43.85227 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c9ffe049-f441-38ee-b4e8-00e1ed6661ba | -20.13421 | -43.85595 | 2024-10-04 04:12:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 225acf8a-69de-3f35-abd1-35aa13c97698 | -20.13259 | -43.84424 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43f2bd4a-e91d-3969-974b-dc532d107c44 | -20.13202 | -43.84795 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bcd95abe-3dc6-3d56-b0a5-06a33917eb2d | -20.13031 | -43.52 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 682d3626-f47c-3d73-8f97-c8e27585974e | -20.12976 | -43.52366 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 5d69bc84-822e-351d-aace-87b97d8db965 | -20.12921 | -43.52734 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 6758480f-3cb1-36eb-8414-0ba3983965a5 | -20.12698 | -43.5194 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f9a93897-3168-3f23-8652-aba4dae0cc9c | -20.12587 | -43.52678 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a8f1d874-8694-3225-8d1b-7859b0f90e97 | -20.12539 | -43.84675 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5adbb00b-1427-36c8-984c-bbd2270caef9 | -20.12309 | -43.5225 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 84634937-9d2f-342c-928e-d55bd30681f2 | -20.12253 | -43.52621 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5d8dc7ca-8e9c-3f39-99c2-2a75e4140b30 | -20.11918 | -43.52567 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 693e8cd6-3c8a-3ff5-bf6c-ec3cb0ea89a6 | -20.11696 | -43.51763 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 87af689a-a226-3091-b8ca-463712bd384b | -20.1164 | -43.52137 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 060e95fa-4941-395d-8fa9-86922b57019e | -20.11584 | -43.52514 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 216731ef-d6fc-344f-9a3f-3923dfb6fcde | -20.11528 | -43.52893 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 50f4dea4-a33c-341a-8a43-2338eae7b132 | -20.11362 | -43.51705 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| bc75d8be-fc75-37b4-84c0-6496e2be251c | -20.11306 | -43.52081 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f8d990f5-d47e-381c-beee-de89a41df594 | -20.1125 | -43.5246 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7f760aaa-af66-3d1a-b1b4-44e1cb2d8f31 | -20.11193 | -43.5284 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 958e1f61-9600-3519-8907-04e6187dc811 | -20.11136 | -43.53225 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ad704817-df3b-382f-9582-9ba80f045a13 | -20.10972 | -43.52026 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7ffdbc92-387e-3151-9789-40ac5c0c9fab | -20.10915 | -43.52406 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 6da84af7-8b84-3927-8bcc-00bb9aa4c79b | -20.10859 | -43.52786 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 04d190f1-e54b-3b42-91fb-3c9b014ab563 | -20.07656 | -43.61028 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 534e309d-b5e6-3c83-9eec-d4b365e13c65 | -20.06938 | -43.58988 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 55fe0d46-b5cd-337b-a8f3-80d3965f7a59 | -20.06653 | -43.60871 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ec9d4d5c-c0e3-37b9-9910-eff407cebfca | -20.06374 | -43.60451 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 42e831e3-a90f-311a-a01c-d841b3976c30 | -20.03492 | -44.14891 | 2024-10-04 04:12:00 | NOAA-21 | SARZEDO | MINAS GERAIS | Brasil | 3165537 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5f86ff6d-6fe0-3eb7-8f5c-c644c849b06f | -20.01199 | -44.49456 | 2024-10-04 04:12:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 04ae7b0a-2f66-3568-993f-d699be964bd0 | -20.01142 | -44.49822 | 2024-10-04 04:12:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d0b5bb00-00b8-3f7c-9fb5-21f4ff9f19ab | -20.00925 | -44.49034 | 2024-10-04 04:12:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| dcee4f8d-6c3c-3996-ab7f-52254b42f3dd | -20.00812 | -44.49764 | 2024-10-04 04:12:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8e3a2706-6fdd-34d4-87c7-516487f120b3 | -20.00595 | -44.48976 | 2024-10-04 04:12:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e58cda88-0524-3269-94b6-1eee6daf3eb0 | -19.99316 | -43.55043 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b6990e61-13be-389b-9ec7-6703482a1893 | -19.9926 | -43.55421 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9ecd9216-38d1-3927-8213-7334cfdce306 | -19.98161 | -43.54142 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 61621068-4545-3214-add0-1ee1601d1544 | -19.89806 | -44.52756 | 2024-10-04 04:12:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7ff9bfe7-9366-3259-a504-f020721b1ccf | -19.89476 | -44.52699 | 2024-10-04 04:12:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 30e53ad8-e8a5-31bf-a325-5fac555cad12 | -19.89203 | -44.52277 | 2024-10-04 04:12:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cfa7e685-f25c-31c7-9cea-39d27762bd60 | -19.89146 | -44.52641 | 2024-10-04 04:12:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e19f6862-31f8-3d11-88b9-08cece804bca | -19.87787 | -44.59143 | 2024-10-04 04:12:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 94b418e4-696e-3fc5-943e-ffc656b266c2 | -19.8773 | -44.59509 | 2024-10-04 04:12:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c9274876-37a0-3d7e-945b-d2a35bc0bc34 | -19.65149 | -44.90461 | 2024-10-04 04:12:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 965f61ce-6a1a-3e90-83ed-16b6ccd96e2f | -20.19497 | -43.81287 | 2024-10-04 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 77cd4084-c001-3af5-9b0f-b58bd1b44603 | -20.14361 | -43.8614 | 2024-10-04 04:12:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1a0c5cf2-781c-360c-bd54-009d199e0a32 | -20.14312 | -43.84228 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8952097b-1b19-3d68-9598-5bb06e9cc1cc | -20.14029 | -43.86081 | 2024-10-04 04:12:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 443bab07-5b53-3cc9-a49c-82a29ca90913 | -20.13866 | -43.84914 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43f69996-a03c-38cf-9b03-973bc63e4b14 | -20.13697 | -43.86021 | 2024-10-04 04:12:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9cd08381-1ff9-3efc-8041-59dcce2db288 | -19.95798 | -43.76186 | 2024-10-04 04:12:00 | NOAA-21 | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b14c3d61-2c32-3bb9-9bde-f7234ca69c68 | -19.88815 | -44.52584 | 2024-10-04 04:12:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 834e7644-a844-3d21-9492-f9fafedae4d5 | -20.12753 | -43.51575 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 76170a45-16f2-34c2-8692-dd634306e8ff | -20.12419 | -43.51513 | 2024-10-04 04:12:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 77b26999-6bc8-3ec0-813e-b7e422c6bbdf | -22.01111 | -44.4942 | 2024-10-04 04:12:00 | NOAA-21 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 00d0ca7d-29b9-3da6-8bfb-71f45d8dea7f | -21.63345 | -44.47473 | 2024-10-04 04:12:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 84d7accd-8d56-36a4-b522-f6cd0762db96 | -21.63014 | -44.47414 | 2024-10-04 04:12:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 295b9364-299f-325e-83df-a1c4a3e0a7d9 | -21.57769 | -45.11826 | 2024-10-04 04:12:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf5059fb-a6d0-316a-b109-86358b79a8e0 | -21.31681 | -44.83033 | 2024-10-04 04:12:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0d9a44aa-fe64-3067-8dca-98f43d86c413 | -21.31624 | -44.83401 | 2024-10-04 04:12:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6328aab1-78b7-36e8-bdf9-5d42c02fc7dd | -21.31351 | -44.82974 | 2024-10-04 04:12:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cba521aa-f866-37fa-9846-60ce4983fcba | -21.19457 | -44.93717 | 2024-10-04 04:12:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2d42a6d7-7b39-3e11-9388-8bb57aac7a65 | -22.01053 | -44.49795 | 2024-10-04 04:12:00 | NOAA-21 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |


[Clique aqui para ver as próximas entradas](README89.md)
