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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be1143ff-9365-3a69-a434-aaa05d7a1aff | -22.362101 | -47.905499 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 533ef02a-123c-3aca-805f-66834b4c0949 | -22.3638 | -47.913101 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b5e584fa-8c9e-377f-8396-0faea5abaa43 | -22.365499 | -47.920601 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e31b2f9a-86d4-3f72-a73e-05e2e1e8ba58 | -22.367201 | -47.9282 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4e6abbc3-1fce-38d5-948a-2bdc8250da86 | -22.357401 | -47.930801 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fdf682f9-9cd7-3cb4-aed7-279750d9f1b0 | -22.3592 | -47.938301 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 181c261b-d93e-3c85-a354-48bfa9c51379 | -22.360901 | -47.9459 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3550ed00-a830-34c9-b409-b4b59d266d95 | -22.3626 | -47.9534 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 64b7829d-2b19-3791-9703-33586c0e2c5b | -22.3477 | -47.9333 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ca855fd2-52b8-37fa-ad14-98f3ff838304 | -22.3494 | -47.9408 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 056c3bc4-056c-3981-a859-1a0555edda14 | -22.351101 | -47.948399 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c92a95f5-1f57-3c1c-88b8-efa8ae429db8 | -22.3528 | -47.955898 | 2024-10-03 01:01:33 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bac1ee8c-ae5e-3a67-9ff1-4c253db17aad | -22.339701 | -47.943298 | 2024-10-03 01:01:33 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1dc08e34-d85d-3da3-b243-e33ae6a792df | -22.3395 | -48.308899 | 2024-10-03 01:01:35 | METOP-C | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c22bdd25-b912-38af-8a09-c8b594ec3802 | -21.455999 | -44.584599 | 2024-10-03 01:01:35 | METOP-C | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6dcdd362-0425-306b-9718-7f28166ac1a0 | -22.3379 | -48.301498 | 2024-10-03 01:01:35 | METOP-C | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 14ec48f3-1b58-30e7-8b2f-9b9cbdbd07a2 | -22.024 | -47.109402 | 2024-10-03 01:01:35 | METOP-C | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8b819cbe-8e8e-3f5b-9a51-5ea132901af2 | -22.0124 | -47.104 | 2024-10-03 01:01:35 | METOP-C | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 04ae4af1-d9c4-3cbf-86a3-dedd0ce8f97d | -22.014299 | -47.1119 | 2024-10-03 01:01:35 | METOP-C | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 30e1dad0-2708-3d23-9b5f-0463b0a7f4d3 | -22.6845 | -50.4674 | 2024-10-03 01:01:37 | METOP-C | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1258344e-abdb-3f3a-87d3-f9780dd9b78c | -22.6861 | -50.475101 | 2024-10-03 01:01:37 | METOP-C | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4a143fb6-73fc-30c3-baaa-866193255c69 | -22.6877 | -50.4828 | 2024-10-03 01:01:37 | METOP-C | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 90663392-4348-3309-87d9-d75c6d56bbf5 | -20.6588 | -41.989601 | 2024-10-03 01:01:37 | METOP-C | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b038346-5735-3d35-bbdb-b5c22748ca8b | -20.6628 | -42.004601 | 2024-10-03 01:01:37 | METOP-C | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31f7c518-2387-3ac0-8af6-167a9c3f3029 | -20.6668 | -42.019501 | 2024-10-03 01:01:37 | METOP-C | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88edd129-5c5c-3561-9aaf-bda145ea5522 | -22.2425 | -48.428299 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d6fe57b5-e10a-33a8-8ad7-1d0d52f352dd | -22.245899 | -48.443199 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 911ec1a3-8373-3db3-bcec-76ec5f2af9fb | -22.247499 | -48.450699 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ef63b54e-bbb6-3ed5-bb44-7e9da084f96f | -22.249201 | -48.458099 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 963db9cd-242b-3e13-a6b0-5cebe15a8671 | -22.2509 | -48.4655 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d46cf823-4fe6-34b3-8188-21654fd73753 | -20.6492 | -41.9925 | 2024-10-03 01:01:37 | METOP-C | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e17816ba-dfb7-39c7-9e65-3145fd929f77 | -20.6532 | -42.0075 | 2024-10-03 01:01:37 | METOP-C | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88eb8daa-2d8f-3fe1-9beb-ebc7263eeacf | -22.2327 | -48.430801 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3b972c80-d61a-30e2-856e-de0487e131ea | -22.2344 | -48.438301 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bdf2fa86-275f-38da-a5e5-2f243c237fec | -22.236099 | -48.445702 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7d0322fe-8c9d-34db-a3fe-aba022e8ac42 | -22.2377 | -48.453201 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ea2f415f-6a28-3a63-86bc-a98e11219734 | -22.239401 | -48.460602 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6b0856-0c5f-3661-8928-31581c44dcc8 | -22.2411 | -48.467999 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d06478e2-f872-3b13-81f3-332e503a383b | -22.2279 | -48.4557 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 21c8142d-3925-3915-b11d-7f65bd57109d | -22.229601 | -48.4631 | 2024-10-03 01:01:37 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1dc1cebc-0485-3bdb-9a7d-4e26f52157f5 | -22.171499 | -48.572102 | 2024-10-03 01:01:38 | METOP-C | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4bbf1361-00a4-34a4-893e-0e8dd04246e3 | -22.173201 | -48.579498 | 2024-10-03 01:01:38 | METOP-C | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd002351-6ead-3281-80b8-ff381e99f31b | -21.9049 | -48.348999 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 74989268-41d2-3970-aa72-bbc329d06a0b | -21.9065 | -48.3564 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5d6b1c6e-ca87-37bb-8e03-c1f8b746816d | -21.918301 | -48.4086 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ccf6ac70-786e-3d77-a2c7-cf2d0b7b2495 | -21.919901 | -48.416 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 22ec5ad4-44d1-3955-9f75-c5d897bd463f | -21.9216 | -48.4235 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f58f8237-10fb-3541-9cfe-20b2d9992a80 | -21.861401 | -48.202 | 2024-10-03 01:01:42 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b7f31f5f-6a53-3583-aed8-8c26413069ae | -21.8631 | -48.209499 | 2024-10-03 01:01:42 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| afea85c5-bd47-3d95-8893-e4c665c2ab6a | -21.8985 | -48.366402 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 39c226b3-7e70-3e63-a8d3-425907e5b65f | -21.9002 | -48.373901 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8bbbd476-7d09-30ff-bb13-1cf38194d716 | -21.901899 | -48.381302 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e98372c9-1bc3-398f-bb4f-2b1566d16938 | -21.9069 | -48.403702 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3400083c-521c-314c-b662-39ac5b0345d0 | -21.9086 | -48.411098 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9e2bf5be-a6fd-3cd0-b17b-39c825a56810 | -21.9102 | -48.418499 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 999884fd-e289-3fe1-bce5-027d2f784f6e | -21.9119 | -48.425999 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 08371108-c254-3f31-8807-2dd405144c31 | -21.913601 | -48.433399 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ddd6d80d-378b-3bbe-a2e8-6396d62460cb | -21.851601 | -48.204399 | 2024-10-03 01:01:42 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c934c837-43fd-3891-b7e3-6ba176313f10 | -21.8533 | -48.211899 | 2024-10-03 01:01:42 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7035ad44-d565-3f63-8607-847d29419318 | -21.886999 | -48.361401 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 049fbc92-c012-3893-bd5d-4b8049fc9230 | -21.8887 | -48.368801 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 83b58930-971a-3a8f-a291-d4540ed9b2c3 | -21.895399 | -48.398602 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d6997a09-fbc0-3ca1-9150-83102d865a40 | -21.8971 | -48.406101 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3dcd55b5-f56c-3e84-bbb7-568a26181423 | -21.8988 | -48.413502 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9eb98b25-bbeb-3bd5-99a0-9dfb5486f182 | -21.9004 | -48.421001 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a1d796d4-64e2-3fb3-807a-c98ae2f7e368 | -21.9021 | -48.428398 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6db7f800-13d4-36fe-adba-9600023d4796 | -21.903799 | -48.435902 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 552ad768-c4e8-380f-b5bb-12004df32d14 | -21.8419 | -48.206902 | 2024-10-03 01:01:42 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5fc5b547-4bd3-3f79-9d54-869dabaef51e | -21.843599 | -48.214401 | 2024-10-03 01:01:42 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0dc83d7b-b5ae-3685-bc46-e24cba3675ea | -21.8773 | -48.363899 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d9e4ce6e-b0b2-3fc4-92b5-db07fe8dd443 | -21.884001 | -48.3937 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 634ed55d-471a-3cdf-90a1-68602ef48935 | -21.8857 | -48.4011 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a7ea949e-1750-3938-b50e-b30a00666d75 | -21.8874 | -48.4086 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 75e7e62b-7923-349d-bb02-e8d26ec91e97 | -21.889099 | -48.416 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 998f9c3a-df2e-3f11-ae97-811df32220ca | -21.890699 | -48.4235 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2e5449e7-eedb-33fe-9cbd-6d6b19cb25ed | -21.892401 | -48.430901 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e1d127a4-8ddf-3347-953f-199b5f3f7725 | -21.8941 | -48.4384 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| da5b35fb-44b3-305d-baac-2e14f6d2c218 | -21.8958 | -48.445801 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 680686df-35b3-3598-a9f8-e9f40981954e | -21.8974 | -48.4533 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ac4417ea-1228-3ef9-9119-f84b6285077a | -21.880899 | -48.4259 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a499ce37-f361-32ec-842c-4af20f9153cf | -21.882601 | -48.433399 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c5d7ff77-36e3-36e7-a94a-fe4510fda67d | -21.8843 | -48.4408 | 2024-10-03 01:01:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 69f0cea1-327f-302c-87c3-f2a16d9908b3 | -21.869499 | -48.421001 | 2024-10-03 01:01:43 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0262d30f-6404-39c0-b5f5-9fe191d28daf | -21.871099 | -48.428398 | 2024-10-03 01:01:43 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c1f065b6-58fa-3f54-add7-3877d2645773 | -21.872801 | -48.435902 | 2024-10-03 01:01:43 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c2ff3787-51a1-3342-83ee-a1b17020b790 | -21.8745 | -48.443298 | 2024-10-03 01:01:43 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 61a1f1eb-132a-3641-960f-8e016ae7a023 | -21.861401 | -48.430901 | 2024-10-03 01:01:43 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5962fc0b-1165-39bb-b361-4185614ce1e7 | -21.8631 | -48.4384 | 2024-10-03 01:01:43 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5432f741-0311-3538-bdb2-9a81310843bd | -21.864799 | -48.445801 | 2024-10-03 01:01:43 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 49b80d59-3173-3850-89c9-afe91f1904c9 | -20.214199 | -42.469898 | 2024-10-03 01:01:46 | METOP-C | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16618110-4051-33d1-b70c-2a958e0a8b09 | -20.218 | -42.4842 | 2024-10-03 01:01:46 | METOP-C | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4aad0323-99da-3283-a7b0-03e50fd6e6c8 | -21.3922 | -47.639702 | 2024-10-03 01:01:47 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d229e2f1-4fa9-3528-aafe-92490c00cbc5 | -21.393999 | -47.6474 | 2024-10-03 01:01:47 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6ffe4611-b975-3514-a6a2-0ff6f45b7d26 | -21.378799 | -47.6269 | 2024-10-03 01:01:48 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c0dc52fc-037f-3f7b-bb99-e3836f403c35 | -21.3806 | -47.634602 | 2024-10-03 01:01:48 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a3a4176b-3473-3b34-8ac0-f20dbfbe7f9f | -21.382401 | -47.6423 | 2024-10-03 01:01:48 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2a38f51d-2950-3355-bb81-fd7e8649a9c1 | -21.384199 | -47.650002 | 2024-10-03 01:01:48 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| de64b8cf-7cbc-3dcd-b12a-b78f9bb08d08 | -21.387699 | -47.665401 | 2024-10-03 01:01:48 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e1357e54-3045-36ef-9832-df4047fa77d8 | -21.3895 | -47.6731 | 2024-10-03 01:01:48 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| eabb3eba-e429-36ba-b694-ffdae9174569 | -21.3727 | -47.644798 | 2024-10-03 01:01:48 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README24.md)
