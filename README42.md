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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34c04821-434b-3dd7-97d2-7930d200242a | -3.96418 | -48.13442 | 2025-08-21 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02083c9b-c9b5-31b7-bf82-9034770cff7a | -2.58445 | -51.92104 | 2025-08-21 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 764589e2-59f6-3e63-a9a0-c8261224b4c4 | -4.83512 | -42.70056 | 2025-08-21 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c8649b8-9a01-32ae-a850-ff37241f64c3 | -8.17542 | -47.32783 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe29bcee-a383-3406-88fa-2a10d69825c3 | -3.0447 | -49.42198 | 2025-08-21 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5156bc8-153e-36aa-92b2-f8043d3980bc | -6.17304 | -44.73459 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 204451e0-9157-38c0-a1fd-1b0a78656f2c | -2.55051 | -47.70755 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16c07e45-066e-38e7-9835-c96817253ce1 | -6.45643 | -53.38348 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a23591f0-a775-36f7-9981-d0041fdff060 | -7.49093 | -44.9434 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87f1b5eb-c181-3246-ae89-fafeb80d28c6 | -8.28359 | -47.28313 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2bffc0e-dff2-3165-9b8b-f1c6a74ee4fa | -4.16646 | -48.57789 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f9ba29e-fe99-34e4-87fa-0c3f0898778a | -6.44895 | -53.38224 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc091f35-7cec-31e1-b3cf-2b9868e46450 | -6.891 | -51.08308 | 2025-08-21 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93b2aea8-cce8-341b-837c-12a27444a421 | -6.62016 | -43.88226 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2d321e7-c97e-33b7-85a5-d9f7d914c446 | -6.0299 | -44.3847 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a27b03b-12f3-3728-81aa-ca87828cd525 | -6.70822 | -44.32315 | 2025-08-21 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7c5494c-969d-305a-b17c-db3962426156 | -8.83404 | -52.06099 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1ba5203a-5e02-3a3c-99a4-2d062ab0e09a | -2.4384 | -48.61395 | 2025-08-21 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efaeaea1-fee4-3c36-9fd1-5a75549a57ed | -3.45676 | -48.96427 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88d6e322-1a7a-3ddc-9b12-d4b7a0ec0293 | -5.85816 | -49.56904 | 2025-08-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03ebbbf8-ecb0-3800-bba9-294a2aa20b16 | -6.00772 | -42.85149 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2bf23581-0b74-3b27-9d9b-62966b9b3fc6 | -8.79682 | -45.43435 | 2025-08-21 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ab712f8-961e-3079-9277-d8f2f8c2d6ce | -7.14175 | -44.17839 | 2025-08-21 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 694dabec-8a09-378c-8563-cd50ea1e0fbd | -7.95116 | -42.6445 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b4e3cb1-385b-3bb4-a788-37cc371a55dc | -6.26347 | -52.81994 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33a5ae66-5f9f-3c05-a351-794bc753b885 | -7.64654 | -46.25429 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c64b75e4-8086-3124-8d86-f40fd2b16bae | -5.87526 | -42.41313 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a2bfee4b-d976-3c5b-8834-681d40041974 | -6.28784 | -43.88036 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13a94c8b-d8e2-3b64-89a4-274c6358a6af | -3.98277 | -42.50816 | 2025-08-21 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c286b5e2-6989-3ef0-955f-882569536403 | -6.42322 | -44.67178 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebff103d-2ae7-3bec-9aed-590e4b849c57 | -8.26418 | -47.29231 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fa9d695-1656-30ec-aceb-3b4e8b63f120 | -7.63353 | -45.25542 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddf3a494-ccfa-3a60-9a2b-186448ed5e4f | -4.31156 | -48.08411 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a06752d2-d66f-3890-9283-6eafa920367e | -6.80531 | -50.08862 | 2025-08-21 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 436f14b1-0c46-3367-8c39-1aa724373c6b | -7.86021 | -46.7293 | 2025-08-21 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| db96622c-ff2e-3ef4-8f58-6641ef14727c | -7.12039 | -44.66013 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eca7609-4bc7-316e-b00d-66bd1ff932a9 | -7.59596 | -55.20004 | 2025-08-21 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fb2e6aa2-b647-319e-9d4b-078347ce81a7 | -6.49569 | -43.10764 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3523a577-d106-3fd6-8931-c8a3eb0ce9c5 | -6.54258 | -45.51499 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f01149bf-c481-3819-922c-1ae0aa1db31f | -3.99166 | -42.50949 | 2025-08-21 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1208d48a-d6b2-36fb-9ff8-d984ea161df8 | -5.99487 | -42.81403 | 2025-08-21 04:38:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 69dc1302-f7dd-3015-be96-faf486f2983b | -6.4271 | -45.4847 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3f33595-e542-3574-b6b4-76ed646e65d3 | -3.03586 | -49.43481 | 2025-08-21 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f393ca3-3433-3987-8deb-45e5eacd35e5 | -9.10905 | -45.18297 | 2025-08-21 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0efee62c-3bf0-317c-afdc-8e880df2cc20 | -7.14278 | -44.59164 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b6683b5-3e6e-3b0c-931f-f4e2c49b2878 | -7.88605 | -46.72892 | 2025-08-21 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a56713c-e313-330c-8042-e59d3925723e | -2.69576 | -48.20987 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75e4fba0-282e-3e33-acf8-87cca16cf8b2 | -2.29196 | -47.99116 | 2025-08-21 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 680e23d4-2890-3aee-a285-d880796283a0 | -6.27634 | -43.72371 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 237490f8-c6fe-3ed0-a9a9-ac4019b8b8d2 | -5.68239 | -43.86364 | 2025-08-21 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44581c9a-60c2-3db3-a672-50ac77979f18 | -7.14777 | -44.17887 | 2025-08-21 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db8c988a-efe7-3984-a755-340d7e1bfd7e | -6.10664 | -44.37437 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6757dfa7-c4d6-3cea-b1aa-4afebe59824b | -7.39174 | -48.18865 | 2025-08-21 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f901dd3b-51d1-355b-abb1-61f56020a090 | -6.00706 | -42.85596 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 956fe5e9-19c6-364b-886a-00bbb3847305 | -7.15012 | -44.17926 | 2025-08-21 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78744066-fed0-3ac4-8f27-c7c2dd6baba1 | -7.24878 | -50.1628 | 2025-08-21 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a55d5568-e642-395e-8d00-6be2cc281bd7 | -5.96722 | -44.14033 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30d86037-332d-3b2d-a0ec-0bd21e08dfc8 | -7.28514 | -49.39441 | 2025-08-21 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18b1bcf7-e12c-32db-b5eb-0398925db99b | -5.96203 | -44.14696 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12cc26f7-98fc-3385-88d7-d4febe85bf4f | -7.94644 | -42.6441 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2481f4b6-f66c-3fd2-9ddd-697dfa49f035 | -4.16977 | -48.57841 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9891aee5-79f9-3744-bcfd-d5e935e16f49 | -6.96904 | -44.15722 | 2025-08-21 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3be85c49-9e2a-3dcc-ae75-b1dd4e2ededc | -8.30704 | -49.02437 | 2025-08-21 04:38:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ee47f99-e0a5-3d32-9329-0c7d042667b2 | -8.68714 | -48.51541 | 2025-08-21 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee9bec7a-bd62-3e80-91ba-92692997e2aa | -7.02152 | -44.62477 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 11fadaf6-ed63-3930-991c-61f3c1cf4054 | -6.50015 | -43.10813 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03c0558c-53b1-344d-b0e1-b48a0a245e5e | -7.0277 | -44.61065 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebb5bc34-f857-3197-9b12-b59715f9f39e | -6.43091 | -44.66266 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfc1a7a9-d09f-31ac-a68a-b798cd985aae | -9.31903 | -48.93413 | 2025-08-21 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 979cf7b9-0189-3690-97df-1c16179a5fe3 | -6.02112 | -42.82258 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da7f1e35-1c73-3e07-b4eb-d62994639fa6 | -4.65093 | -43.12334 | 2025-08-21 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de45aa80-bd02-3bfc-8cbe-66d4a7ed43a2 | -7.85161 | -45.19025 | 2025-08-21 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab14ff27-d343-32c4-a38c-c595096b2067 | -4.55239 | -50.45909 | 2025-08-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84109c44-d1e0-3e79-9719-38334435a38d | -2.44307 | -47.32621 | 2025-08-21 04:38:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b3510b8-bede-3f36-b3bf-fa5c0b0cdd66 | -6.01995 | -44.36854 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0824098-269a-3f4f-8d44-afdb3da608b2 | -2.58727 | -51.92299 | 2025-08-21 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9228964c-72a9-389d-a7e9-64233805b4d8 | -2.54219 | -47.71702 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34d02089-2d12-304b-9451-0e81c83013c9 | -7.63425 | -45.25056 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa382f07-ed53-3658-beb2-8e5165b51ecd | -7.57366 | -44.39653 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e7bc02d-a2c5-387f-99a0-ee28863a97cb | -9.33065 | -48.51944 | 2025-08-21 04:38:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bc58fc4-0e5e-3a81-898c-bda69e2b0588 | -7.64958 | -46.25918 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b13d42fc-3504-307f-ad59-fa01a2728a35 | -7.70402 | -44.02798 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94dd6292-9546-35a9-8ece-2d829359e56d | -9.48429 | -47.32532 | 2025-08-21 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56b69e84-ec74-331a-a5ce-8d350f3496de | -8.06898 | -43.68467 | 2025-08-21 04:38:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bccd805d-4c0e-3e76-9170-140b9c21fa89 | -2.38164 | -47.65961 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19a7cdc1-9498-3ea6-bed5-616662673c59 | -6.50144 | -43.44407 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e375350-e19f-3206-9b07-8983c9e1ecfa | -6.95712 | -42.86316 | 2025-08-21 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fc32682e-f927-3e30-81fb-80fc2545ae84 | -6.07011 | -44.14021 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5788687c-1822-3cb9-a3af-e3d37cb74f8e | -5.12741 | -42.94083 | 2025-08-21 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26fa06fb-485f-3af8-8578-cf4d91a76430 | -7.41706 | -46.86926 | 2025-08-21 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e8ee3ab-9e43-3a1c-9531-eba35891a8c8 | -7.20949 | -45.31174 | 2025-08-21 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6ef1673-1a6b-3a96-875a-c5cb85e8b017 | -4.91261 | -45.31878 | 2025-08-21 04:38:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07cf88e3-6784-3e37-b92c-ee5b175be183 | -6.53946 | -55.3078 | 2025-08-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e44aa61e-990e-3dbd-93ba-bacc6580ca90 | -8.34806 | -47.50101 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d5433a7-cee3-34f4-b721-c4930e1b728d | -3.03696 | -49.42787 | 2025-08-21 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f665dc0-9b5a-32c0-9138-2dc6be826524 | -8.35095 | -47.50547 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bcba089-e161-3ed3-ae69-0700ee5c20a3 | -6.36073 | -43.6517 | 2025-08-21 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28259ae3-51bb-32b8-9c08-dcc3770d910c | -2.8226 | -47.72416 | 2025-08-21 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b896038d-89cc-36e9-bcce-3f258bb219e0 | -5.95901 | -44.13921 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c80d4ce1-8d22-3be6-8068-854910ddfd41 | -5.80217 | -42.93734 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README43.md)
