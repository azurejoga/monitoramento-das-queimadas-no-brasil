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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 582a07dd-4d82-3b51-b56f-ebfe3de36cf4 | -11.42329 | -54.29963 | 2025-03-29 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17cc9253-c9bb-34c0-b0d4-e6a288a22ce2 | -7.23274 | -44.77821 | 2025-03-29 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef3858b4-9685-386e-b525-4ecd56f58183 | -19.14063 | -51.56721 | 2025-03-29 04:57:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9db7a723-ba4d-36d9-bcdf-6edbf1352d7e | -18.53702 | -56.18661 | 2025-03-29 04:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a04d7982-887b-316d-b8b6-bcd3724cbc1c | -18.37759 | -47.35873 | 2025-03-29 04:57:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1caa0572-cdb3-390f-bd06-a61188b74f9f | -19.88766 | -48.35672 | 2025-03-29 04:57:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9778cabe-ac19-3426-8eeb-66d20183359d | -18.53758 | -56.18296 | 2025-03-29 04:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3eb04567-56b4-326c-a1d1-5ca741ef8d17 | -12.61084 | -52.1222 | 2025-03-29 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1e27044-97e8-3f5a-a7b5-e958f1586887 | -12.61207 | -52.11357 | 2025-03-29 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 565a5e70-b4bf-33c5-b61e-4a458d16162a | -20.13566 | -50.72025 | 2025-03-29 04:57:00 | NOAA-20 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7eb89d09-c0b3-3b6a-ba7b-d782c82be527 | -15.85562 | -54.12615 | 2025-03-29 04:57:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a26661a6-5645-3b0d-bc07-d4e513e06afa | -18.57318 | -55.53028 | 2025-03-29 04:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| db490b88-13b6-31bd-a41d-e7b5f514458f | -19.14438 | -51.56605 | 2025-03-29 04:57:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc8566cb-efeb-3249-a1a7-95c71e2b488f | -18.53426 | -56.18239 | 2025-03-29 04:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 00e58d3a-54fe-396f-811b-ab6939b1de42 | -15.17737 | -52.29357 | 2025-03-29 04:57:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e7a10f3-1294-3f96-87ad-29259041e144 | -18.37723 | -47.36218 | 2025-03-29 04:57:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3b24311-8b62-314e-9fc1-cb8613f26b79 | -19.88832 | -48.35058 | 2025-03-29 04:57:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9245f8da-58e9-32d2-9408-a840db7ffa21 | -19.88799 | -48.35365 | 2025-03-29 04:57:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b572932d-4954-34dd-858a-f88ef6cbea03 | -12.61145 | -52.1179 | 2025-03-29 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51176471-a9ec-3604-abab-a142d98a836c | -19.14031 | -51.5654 | 2025-03-29 04:57:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d510fd84-2c86-308b-b1d1-ba3eb37c98ad | -15.60125 | -57.34531 | 2025-03-29 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4360ce53-6180-3f01-ae8a-dc27b0149fd8 | -15.85906 | -54.12666 | 2025-03-29 04:57:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2137e286-100c-34aa-8a57-c5401a251664 | -15.85848 | -54.13052 | 2025-03-29 04:57:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 227b60fd-17ff-3772-aeaf-e6fcfe5e5998 | -21.45839 | -57.15647 | 2025-03-29 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 786c471b-374c-34f4-b8bf-2b25e1182a33 | -21.19926 | -55.65279 | 2025-03-29 04:59:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6384ba1d-6108-3ee1-b108-792d99156b37 | -20.9847 | -47.3581 | 2025-03-29 04:59:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6720f80-3db5-3744-9859-319a138d9092 | -21.23564 | -56.46377 | 2025-03-29 04:59:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dab8c408-f6a2-3680-aab2-0cfd0a5b23a4 | -19.87883 | -54.66725 | 2025-03-29 04:59:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30ffd96f-9a8a-3e1c-88c5-d71eb145c70c | -20.91745 | -56.54955 | 2025-03-29 04:59:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fc57c95-f44e-3da6-8d4f-52a5ab84271d | -20.61066 | -55.70723 | 2025-03-29 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4255cdd4-1015-31e7-9cda-c7917f762989 | -21.16758 | -56.48292 | 2025-03-29 04:59:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a070421b-a7a1-39bc-98fa-0544de1dc2ff | -20.57936 | -56.0424 | 2025-03-29 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7b1dc9a3-922c-3bc0-8680-4edab4b563e6 | -20.56928 | -55.08527 | 2025-03-29 04:59:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b28c1098-5598-38a1-a3c5-5d5f17d9ced1 | -20.57993 | -56.03859 | 2025-03-29 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4cf49c1d-2ff8-33e7-a2ff-c8e5d371d6a9 | -21.45782 | -57.16018 | 2025-03-29 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1b8c0ed-09f6-3ed8-9367-ba0cd0063883 | -21.46503 | -57.15764 | 2025-03-29 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15275930-140d-3e8d-a3ab-3af270e81719 | -19.88291 | -54.66369 | 2025-03-29 04:59:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8495f0f9-67bb-3049-b21d-7b72e36ba2d7 | -20.58386 | -56.03536 | 2025-03-29 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27f495ac-892c-35ce-b9ba-d04679249e8d | -20.57657 | -56.03803 | 2025-03-29 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 959a0ff4-53d0-3623-a213-a3b4608fab97 | -21.46171 | -57.15705 | 2025-03-29 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ba11260-a125-3621-838f-af0f0cbfbc74 | -21.46114 | -57.16076 | 2025-03-29 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9b63d00-a7fb-355a-880a-2bf4c428211a | -20.58049 | -56.0348 | 2025-03-29 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1da81b34-a460-3c64-8a7c-f98d1790ba83 | -20.92079 | -56.55013 | 2025-03-29 04:59:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b84de5e6-bbe4-30c5-829d-17bc3f2df816 | -20.56869 | -55.08932 | 2025-03-29 04:59:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2df24ec6-1ed6-3e44-a530-831ddbfe8b12 | -22.15055 | -56.12462 | 2025-03-29 04:59:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b98451c-fff1-325b-97fd-d3efcdfa46ce | -20.58329 | -56.03915 | 2025-03-29 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a134aa29-5532-3297-ad93-8fa468b1ad36 | -20.99022 | -47.35846 | 2025-03-29 04:59:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1b1332d-9a97-367f-8e4c-504fd77a35b6 | -22.15451 | -56.12133 | 2025-03-29 04:59:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c502de8f-5227-36b3-906e-f8d30c22717c | -20.576 | -56.04183 | 2025-03-29 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5d7b2b0c-4f82-340a-a0ae-edf1aeb715fc | 4.08953 | -61.56548 | 2025-03-29 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2a39cf4-ecda-3baa-b6de-da3151d67686 | 2.01401 | -61.09325 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fb320b2-12be-3e4a-b8eb-9c2773bfed20 | 2.00879 | -61.08476 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd4621f1-cbbe-3c6b-b55a-34d5841293e4 | 3.87607 | -61.49981 | 2025-03-29 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 638dfca0-cc2f-39e6-ab82-4685d8bf9b4e | 3.87475 | -61.49158 | 2025-03-29 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ad28f78-d6e4-35ce-aa20-c1288a98da43 | 4.08888 | -61.56143 | 2025-03-29 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7c4f2f5-d76e-3788-beaf-77a8ba5a1ecc | 2.01328 | -61.08871 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0beb7a4f-3e9e-3c8e-aed6-49e56049b25c | 1.94549 | -60.83224 | 2025-03-29 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e843e7f3-979b-36ba-83d9-d94c1d1897e0 | 2.1807 | -61.80775 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e42720e-fd71-3e11-817a-01a2d8cad875 | 3.879 | -61.49513 | 2025-03-29 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fb64092-633f-3000-80ae-7bd6103b6472 | 2.01474 | -61.09778 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c2f61a5-c770-3f7c-bc6e-fe11ce493064 | 2.00536 | -61.09222 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53b6fed7-eab2-336a-b01a-a96592e81683 | 2.30676 | -61.60601 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e45b8b87-4aa9-3e22-81e1-fe7115fab14b | 0.8259 | -60.5866 | 2025-03-29 05:46:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3818b66-80e2-33d8-ba58-767c2530c52f | 2.15094 | -61.82954 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbf1f628-e544-385c-95df-6964c67ef1ba | 2.00576 | -61.08989 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ebcec181-76b9-34a3-87fc-c5abb260e1d9 | 2.30972 | -61.60124 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a8a2eab-4bf9-3b2c-a197-2d6c62c1ce8e | 1.15785 | -60.50137 | 2025-03-29 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a3886ab-e964-37e4-b432-2c7779776cf4 | 2.3072 | -61.61288 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c377c400-a00d-3bc0-ae6c-60f247c77c37 | 3.66841 | -61.85874 | 2025-03-29 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42fcb92a-9a31-3543-9cf8-03c410ec16c2 | 2.31019 | -61.6081 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d0d2565-47c0-355a-8235-d3b4c183fab0 | 0.82984 | -60.58599 | 2025-03-29 05:46:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdfbb5e3-bd7a-3961-9d78-3da3caf4eb17 | 3.87834 | -61.49101 | 2025-03-29 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a545df9e-ee21-3b12-8908-6a8b438710b5 | 2.01357 | -61.09557 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 535ab800-2fb9-3b30-8496-2ac870f6f83b | 2.01146 | -61.08188 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c046258d-c0af-3785-b92d-060fdc3b4680 | 2.0077 | -61.08249 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c61f99e-7e4e-3502-8813-f7795cbbf38b | 2.00503 | -61.08535 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2f9039e8-0df6-363e-a676-f1669751fb96 | 2.30655 | -61.60863 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf06950a-e82d-3a97-b0b5-fccad654d89a | 2.17775 | -61.81247 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e008130e-8748-3658-8eaf-762023f8fbda | 2.00911 | -61.09162 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df64b4d0-8f62-3d9f-81db-faa71585cac5 | 1.94167 | -60.83285 | 2025-03-29 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc824463-ced7-3489-88d0-60af8618954b | 2.01703 | -61.0881 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da3cf47c-8433-3d4f-ba2d-7ce811aab06d | 2.00465 | -61.08765 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2441a5e0-9ce8-38ba-b0ca-7e6203c00bfd | 2.01254 | -61.08416 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1949deb-47b1-3abf-a892-25e8f8741753 | 2.00952 | -61.08931 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36c5591e-df6c-3778-9987-6551a2d3a0b9 | 1.15844 | -60.50259 | 2025-03-29 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da0292f3-2aae-3189-aef9-459071f98388 | 0.82667 | -60.59163 | 2025-03-29 05:46:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e090a77-219b-3c0c-a74b-af9fd44d42b8 | 2.01217 | -61.08647 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7822a0a1-5d7f-3c01-8322-4a0e5f2a01ab | 2.01025 | -61.09385 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9400262-287d-3af7-a8dd-988b07b19261 | 2.00315 | -61.4427 | 2025-03-29 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d1c4a19-dd09-3515-89ad-2025b08a9c54 | 2.3104 | -61.6055 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5154e87-eb37-3b33-b4dc-2e4181227b35 | 2.01287 | -61.09103 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 301301e6-0f9c-30fc-b251-1ed9a17083d5 | 2.30953 | -61.60385 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47b14978-d8be-3e9b-9a5f-584f6e490f32 | 2.00841 | -61.08707 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 603f384c-7ea5-391d-9159-ba0ed595f4a9 | 2.30745 | -61.61027 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39451b75-a1c6-32be-ab46-2890e6a9abb1 | 2.18201 | -61.81605 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c75cffa-0f07-34de-9376-995dad022af2 | 2.73372 | -60.39473 | 2025-03-29 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ba7582b-a583-325a-abc1-1dc9b19f8ee5 | 2.18135 | -61.81189 | 2025-03-29 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a801109-44a9-3920-ba3e-e11aad291348 | -15.28259 | -60.22334 | 2025-03-29 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a63c3f9b-89f9-3bf8-99a8-917fb2ad3134 | -10.52449 | -67.83494 | 2025-03-29 05:50:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46f10821-7d69-350d-936c-3392ef585f34 | -9.2601 | -60.31488 | 2025-03-29 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README5.md)
