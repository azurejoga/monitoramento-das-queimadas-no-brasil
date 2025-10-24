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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6027b4fd-ffa3-302b-aa36-1b660993165e | -21.96317 | -47.93878 | 2025-10-24 03:51:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dc1cbfd0-78dc-34a3-95c1-e52735465eb2 | -17.65085 | -46.66569 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 76e97033-af72-3c14-bf1f-35832311c521 | -19.64974 | -43.63139 | 2025-10-24 03:51:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ce2d7db-4b8d-3e66-a778-2a2c135d97db | -18.57666 | -44.03866 | 2025-10-24 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd58bca5-77e2-34f4-85d7-9e79970979a9 | -21.5204 | -45.98018 | 2025-10-24 03:51:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8fdac7d6-0c54-3679-9d08-b2cc8ec14a2a | -20.70688 | -46.27086 | 2025-10-24 03:51:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b51dacc8-7bf0-38c2-ae83-1d3a963aa537 | -20.1345 | -41.79805 | 2025-10-24 03:51:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 75a5fef6-61a2-3abb-8cdd-2aabe9f692d6 | -19.44462 | -49.32822 | 2025-10-24 03:51:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad0cece1-dbd4-32da-b3ba-6f1f30aeba71 | -20.78298 | -44.86797 | 2025-10-24 03:51:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3b0edeb7-8aca-3e26-a755-38047a4fbae0 | -20.579 | -45.8897 | 2025-10-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 251726ce-2476-3371-8c5e-f6e824117c5d | -20.30742 | -45.77418 | 2025-10-24 03:51:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60bf2557-bdbe-357d-aa04-d5d67704780c | -22.89341 | -47.74707 | 2025-10-24 03:51:00 | NOAA-21 | SALTINHO | SÃO PAULO | Brasil | 3545159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d506ccb8-cffc-3fc0-951e-bd2c46f18e19 | -17.09445 | -46.18659 | 2025-10-24 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb481dde-219c-33c9-a211-553f2bb6974f | -21.76485 | -52.26629 | 2025-10-24 03:51:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 269f7e14-c2e8-3add-b028-1c744cb6dbea | -18.91845 | -47.22213 | 2025-10-24 03:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb6ea240-8b84-3e91-8938-ab2a11a8b4e3 | -20.56099 | -54.65864 | 2025-10-24 03:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 197eefb6-4590-3897-8572-a302d4e6be67 | -21.76375 | -52.271 | 2025-10-24 03:51:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 668b446e-8c51-3b8f-afaf-9b6f556ce95e | -19.28823 | -49.29557 | 2025-10-24 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfb9920e-4fd0-33da-bb7d-e748ae6e467e | -17.64988 | -46.67062 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c181138c-5c62-3e9e-909c-98ccd0e32f57 | -20.20734 | -45.80328 | 2025-10-24 03:51:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc482f20-c024-38b1-9dce-14b31cc89144 | -19.15694 | -51.86411 | 2025-10-24 03:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c527572b-9f7d-32b6-8b8e-25933fa69590 | -18.35952 | -51.71266 | 2025-10-24 03:51:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42e28e49-7d04-3406-9c91-9675226c4eae | -18.46845 | -44.4506 | 2025-10-24 03:51:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 22e16eac-ce99-32e0-8a46-acff3d236c8a | -18.91267 | -47.17816 | 2025-10-24 03:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a628ed82-df33-3256-ab59-5a8f321ae7f0 | -17.59605 | -46.63129 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c9c19b7-57ef-3d5d-86c4-19b4033aefc6 | -19.98618 | -44.22893 | 2025-10-24 03:51:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 53360322-fb32-3b50-bd32-d9df93c9ec91 | -18.45761 | -44.44305 | 2025-10-24 03:51:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37e98ae2-cd94-3f85-a6c1-b4d1281688dd | -23.17031 | -46.72324 | 2025-10-24 03:51:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 97da454d-872a-3c79-9127-691bcb0d6b1d | -17.65544 | -46.6666 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 453a177e-572a-300c-93d3-8b1ca43663ec | -19.59433 | -43.74685 | 2025-10-24 03:51:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ef8b94a-5206-3a98-83d7-f543e56d76ca | -17.47351 | -45.99142 | 2025-10-24 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5956879a-da1a-3ea5-bd19-e38f4c575c78 | -19.60261 | -43.69115 | 2025-10-24 03:51:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26f0f750-8c25-33f1-ba9a-425f7cbc57e5 | -21.96231 | -47.94076 | 2025-10-24 03:51:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 66d5e046-f40b-3fee-aed6-726e72d2ec58 | -23.58838 | -46.41184 | 2025-10-24 03:51:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9fefcdd6-c538-3b41-b0fb-2cc93397a8c8 | -17.59243 | -46.62542 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 164cb95d-55c9-3af3-a407-6884bd455d0c | -20.20657 | -45.80725 | 2025-10-24 03:51:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b49839a1-6e19-3ff9-92cf-60eeb93941f9 | -21.94366 | -42.9345 | 2025-10-24 03:51:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2bb14a4d-57e8-37b5-8a84-838d32c715c9 | -20.58317 | -45.89032 | 2025-10-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf51b3ba-e9e4-3c9b-aa2b-e0c19a515fb7 | -21.80562 | -42.51067 | 2025-10-24 03:51:00 | NOAA-21 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a182c303-c1e2-338f-b808-22f6a944d9e8 | -17.71457 | -46.20083 | 2025-10-24 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f0bd2a4-5499-31ae-b123-6a4547987c17 | -22.80968 | -43.3949 | 2025-10-24 03:51:00 | NOAA-21 | NILÓPOLIS | RIO DE JANEIRO | Brasil | 3303203 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e478e7e4-3b8c-363b-a978-98323fa7fc3c | -22.14069 | -45.64204 | 2025-10-24 03:51:00 | NOAA-21 | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3bdc8aa7-2305-3ce5-a672-b82f7056a7bd | -19.28816 | -49.29245 | 2025-10-24 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92285faa-53ab-3a80-9456-097ff0b01afa | -19.44987 | -49.32937 | 2025-10-24 03:51:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bbb5820-e157-36c2-afb8-1efdbdbf6cf9 | -17.65446 | -46.67154 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46ccb577-9591-37e1-aed7-67f7dc8b7983 | -17.04036 | -51.50037 | 2025-10-24 03:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4149f750-4cff-35ab-8969-f7e7abc6dc7b | -20.41052 | -44.06047 | 2025-10-24 03:51:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 122039fe-8126-3cfb-970e-4f2262763685 | -17.47264 | -45.99597 | 2025-10-24 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79065eca-c327-39aa-bfd4-e9b3f8696aca | -20.13111 | -41.79742 | 2025-10-24 03:51:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 7294a1cf-c7dc-32cb-bef1-18a2eaee921a | -18.36071 | -51.70741 | 2025-10-24 03:51:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d3dc34e-6c8e-31d7-b692-5991a54f5a69 | -20.2381 | -43.60839 | 2025-10-24 03:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c33898b7-f2e2-300f-97c6-16970c062a72 | -19.89217 | -46.95931 | 2025-10-24 03:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b59876a5-68a3-3b43-b839-ea3117c4c207 | -17.60158 | -46.6273 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c079bdfc-f85d-3cda-87c4-b06106aac2c0 | -20.44005 | -44.13766 | 2025-10-24 03:51:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 47365bf6-5794-3fae-b444-3cd8444c0b8f | -17.21177 | -47.65645 | 2025-10-24 03:51:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32180b38-9c39-3013-a919-083012f9b27b | -20.48692 | -44.37204 | 2025-10-24 03:51:00 | NOAA-21 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5429f54c-473c-3a61-b746-e1b04605243a | -18.13408 | -44.46647 | 2025-10-24 03:51:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28263859-be55-30e0-b24d-d5b6f5a91531 | -17.23944 | -44.11314 | 2025-10-24 03:51:00 | NOAA-21 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c8d4338-b435-3c42-b575-87765e554d87 | -21.12664 | -45.73008 | 2025-10-24 03:51:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1aa06ccc-e18b-30ab-aea0-8a50deb386a6 | -20.41108 | -44.06318 | 2025-10-24 03:51:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cc91748d-0ebf-3a75-9e52-a31e84f2a760 | -18.80218 | -44.8113 | 2025-10-24 03:51:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea55bd52-10d3-36ad-8d09-d820b122a2cb | -19.7728 | -46.19698 | 2025-10-24 03:51:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62e7f9d7-cfad-30b2-a8f1-9ded6f958277 | -16.48441 | -47.81961 | 2025-10-24 03:51:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5022e863-2d68-3725-a12e-c6cf1e311d12 | -17.65837 | -46.65178 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b0a8b7e-40e8-3cd5-aeb4-a75a48d0b17d | -17.60254 | -46.6224 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fee872c2-2acc-3884-9f06-60080c48ca84 | -20.71107 | -46.27194 | 2025-10-24 03:51:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bca77c4-bc98-3180-af22-b3777246d19a | -19.76527 | -41.1837 | 2025-10-24 03:51:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ae53d945-031a-3a79-b918-dab165478b30 | -20.36006 | -45.80104 | 2025-10-24 03:51:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc40aa99-651c-359f-b881-5079a0047ebd | -18.60556 | -51.78757 | 2025-10-24 03:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2aff1e03-cb91-3adb-a79f-4601f9d5cb3c | -19.4656 | -41.56996 | 2025-10-24 03:51:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b5262aa3-b7d6-3c3c-aef2-15eec9de77b9 | -19.8877 | -46.95839 | 2025-10-24 03:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6aa5cd1-5cf9-3412-9973-9c56d06fbe56 | -21.22072 | -44.97409 | 2025-10-24 03:51:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 20752678-53c0-3d58-a76f-4eaf2e9a028f | -18.35461 | -51.70567 | 2025-10-24 03:51:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e3a4607-5b07-301a-aa1e-e4264588dc38 | -22.89437 | -47.74242 | 2025-10-24 03:51:00 | NOAA-21 | SALTINHO | SÃO PAULO | Brasil | 3545159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c63aba71-1fa7-37e0-b2b8-0ebf615ae876 | -18.01188 | -47.63734 | 2025-10-24 03:51:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 862801e0-d4e2-32e0-8760-028c88ee03a2 | -21.13069 | -45.73093 | 2025-10-24 03:51:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ee4a25e9-670a-3120-b5d1-9cca2f510d7a | -19.49893 | -44.23036 | 2025-10-24 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09abaf65-571e-3dfe-8c57-eb2895f9e9a3 | -19.46495 | -41.57382 | 2025-10-24 03:51:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ecd9f2cd-bd83-3cec-8c4b-d78d8895c638 | -18.20234 | -47.65032 | 2025-10-24 03:51:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85078dde-6c90-3f34-a930-cb6021667f1f | -20.56004 | -54.65489 | 2025-10-24 03:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d09e0e4b-0e76-32ed-a7c2-373ec4d29f74 | -17.90862 | -45.90742 | 2025-10-24 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6fc9012-2629-354a-bdca-a7389cd1c1f0 | -19.1557 | -51.86946 | 2025-10-24 03:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fb7aaec-c3af-3e50-bb27-d8d6b29822d9 | -22.75284 | -52.19463 | 2025-10-24 03:51:00 | NOAA-21 | INAJÁ | PARANÁ | Brasil | 4110300 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| dff34f9a-ebd0-3437-bf82-c8fb0105ed88 | -19.28891 | -49.29229 | 2025-10-24 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd5ea4a9-e748-3007-bd9e-bffd9dca8e3d | -19.03841 | -39.88343 | 2025-10-24 03:51:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 36f10f6d-eb2d-3f4c-a529-a45bbe7c36f9 | -17.03795 | -51.49894 | 2025-10-24 03:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ddf3c06a-9b0b-3764-aea4-c2071f462f8f | -22.97869 | -47.39772 | 2025-10-24 03:51:00 | NOAA-21 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5cc0b67f-c582-309a-9066-ee7410657a6a | -17.59796 | -46.62144 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c42ebfaa-ef35-34bd-8661-c1d35f1f334a | -19.99087 | -44.22473 | 2025-10-24 03:51:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7ee74538-c8b8-3da1-8d49-afa189e7ceca | -16.957 | -53.22151 | 2025-10-24 03:51:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 181480d5-3557-3066-888c-0a50c9b8c97e | -16.48377 | -47.82281 | 2025-10-24 03:51:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8ab848b-0314-3696-b4be-3dc6d087e3d6 | -21.13143 | -45.72706 | 2025-10-24 03:51:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c4a1b749-9d63-3cf3-939d-0509a5d0ac5e | -21.96212 | -47.94396 | 2025-10-24 03:51:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| df744a15-be60-3341-9f44-5c7ceb2ad641 | -19.28746 | -49.29573 | 2025-10-24 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea06fd11-6ff0-3dd0-9edc-b867e453583a | -18.20463 | -47.64773 | 2025-10-24 03:51:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4190fde-dcc8-3833-9bd4-86227116887a | -21.49878 | -44.09629 | 2025-10-24 03:51:00 | NOAA-21 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 354fdbdc-f6c5-37e4-8371-44d17daaf4ec | -17.09802 | -46.19222 | 2025-10-24 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3e93d78-3477-3b08-813d-ddf384dca455 | -17.60062 | -46.63225 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f24e1072-39eb-39c0-94f2-fd496030763f | -19.7948 | -44.12299 | 2025-10-24 03:51:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae332aa4-d19b-3642-8721-3bec54976b95 | -19.60344 | -43.68642 | 2025-10-24 03:51:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README14.md)
