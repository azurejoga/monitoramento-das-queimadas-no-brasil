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
| 0e959ce6-0ec2-3ce1-bab6-972cb53e031a | -16.58831 | -58.21756 | 2026-02-28 05:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7b053c2e-c086-3a3d-9279-54fd63e65c2c | -21.17037 | -56.49561 | 2026-02-28 05:03:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 456b9575-e201-3473-9a85-d51d9dc58e22 | -23.6391 | -53.2136 | 2026-02-28 05:03:00 | NOAA-20 | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 62faf80c-ec08-3926-ad4d-3a8678425403 | -21.68918 | -56.32063 | 2026-02-28 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d28333a5-eabb-3926-88da-fa4b1595454a | -21.68943 | -56.32377 | 2026-02-28 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fcb032d-f706-32b7-a5ca-ec6bee0771c5 | -19.39611 | -55.10543 | 2026-02-28 05:03:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 841ae754-8ab1-3d32-98fb-3eb7e82b2e4f | -21.68241 | -56.31948 | 2026-02-28 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0385596-6964-3bd1-903e-d523e7919b43 | -21.80166 | -52.72213 | 2026-02-28 05:03:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 012cfacd-cf07-33b3-a701-5db691495573 | -20.52007 | -50.83143 | 2026-02-28 05:03:00 | NOAA-20 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 971863d4-c64e-3cd5-a224-5b748b4187fa | -21.68803 | -56.32837 | 2026-02-28 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 021f15e0-ca62-3f21-9b23-89488d5fb047 | -19.80078 | -55.06823 | 2026-02-28 05:03:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a843789a-735a-3aa3-a55f-53e84ab2ac31 | -22.2238 | -57.09098 | 2026-02-28 05:03:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e659e06-ac02-3181-8e0b-8f35dec552b3 | -21.17373 | -56.49618 | 2026-02-28 05:03:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 476ce44b-218e-3cdd-a4f8-f340415df789 | -20.51952 | -50.83611 | 2026-02-28 05:03:00 | NOAA-20 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| c0dc93ea-b5a9-3047-813d-4028edf9bc89 | -21.68184 | -56.32335 | 2026-02-28 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55906870-ab8f-3417-8d21-fe7152b186bb | -21.22783 | -56.2498 | 2026-02-28 05:03:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4da951e2-0b49-3ad5-9291-e0f6d09b3b0e | -20.51507 | -50.83554 | 2026-02-28 05:03:00 | NOAA-20 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 152c182a-0c8b-32b7-a0bc-a6ca9ca55820 | -21.68579 | -56.32007 | 2026-02-28 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 158c7f7a-dafa-3aae-a493-376ba6257920 | -21.69 | -56.3199 | 2026-02-28 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bf1ffa9-6081-3cf0-9270-ee4e20934a5b | -21.23121 | -56.25035 | 2026-02-28 05:03:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b45d296-066e-357e-beb8-23aad429697a | -21.68522 | -56.32393 | 2026-02-28 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| baed7392-d149-3c61-9b66-caea92ffc009 | -20.51897 | -50.8408 | 2026-02-28 05:03:00 | NOAA-20 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 8d416502-f1d7-3039-80f0-0a3303d3d5c1 | -21.17709 | -56.49676 | 2026-02-28 05:03:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd371d25-c7a0-3091-a0a4-8bbf7a9b9806 | -20.51452 | -50.84023 | 2026-02-28 05:03:00 | NOAA-20 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| c610cb87-8b65-303e-aa2d-1aa620f91e88 | -20.52397 | -50.83667 | 2026-02-28 05:03:00 | NOAA-20 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 634f9c0e-0cc4-395c-991a-77262492bf61 | -21.79763 | -52.72161 | 2026-02-28 05:03:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1c9de47-e3cc-3cb3-87d3-76da05824eca | -21.6886 | -56.3245 | 2026-02-28 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 66424bd9-223e-3154-a005-987cab86d851 | -23.28044 | -55.32764 | 2026-02-28 05:03:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2efd5173-a437-3d8b-abb3-892bb9cf99a1 | -20.51061 | -50.83498 | 2026-02-28 05:03:00 | NOAA-20 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0cad2155-2a74-386e-aa23-55d37a19a378 | 1.4864 | -59.9117 | 2026-02-28 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.3 |
| b4d37014-9a35-3d8b-9b24-bf51b996aed3 | 1.5046 | -59.9306 | 2026-02-28 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c3bb08e9-eee5-3ea6-9145-4999db684301 | 1.4864 | -59.9308 | 2026-02-28 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 119.1 |
| d0031743-f23b-3c37-90ef-60bf4d49b04b | 1.4681 | -59.9309 | 2026-02-28 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 480bc87c-e0cb-3597-a0fb-bbb7cf172380 | 1.4682 | -59.9119 | 2026-02-28 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 5b002f39-62b3-3108-89fe-8fe124561c1f | 1.5047 | -59.9116 | 2026-02-28 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 5113c179-ebbd-37f6-ac24-f3d9734d38da | 3.43058 | -59.8581 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60ac82bd-3adb-3b88-a866-a3efec8b951e | 4.80646 | -60.16265 | 2026-02-28 05:46:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6185653f-939f-347c-b72a-c89d184fa5c7 | 3.09928 | -60.29564 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 325b2ed9-12bf-31a5-83b4-b9cb4f8f1156 | 3.049 | -60.28527 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09bbe82c-b704-3dfc-be28-4e6048b42715 | 3.37641 | -60.54293 | 2026-02-28 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d55d1d4d-7b0c-3110-b872-947c7a1b6880 | 3.37328 | -60.59642 | 2026-02-28 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2015ffa0-3f3a-398d-aeab-9c89249db302 | 4.5495 | -60.88379 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb4cfe83-3606-3824-a771-f5446e9bbd3a | 3.0633 | -60.27108 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fb4d2bf-b94f-365b-ad87-9276a0a0892b | 3.05333 | -60.01166 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c770b0db-99f3-3581-beda-4acc78cdf68f | 3.15273 | -59.90313 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed74e432-df5f-3409-bdc0-c43f613a71bb | 3.0451 | -60.28593 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27431a84-b823-355b-b48c-bb484b05f883 | 3.65285 | -61.0983 | 2026-02-28 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7db1c15-cf89-3a22-aa36-0518da1a6eeb | 3.43001 | -59.85464 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e515c60-3817-336b-96b6-23fa9df72b88 | 3.42661 | -59.87353 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c40d9aee-e25e-31ec-87a1-97e3236459ad | 3.14986 | -59.91071 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9dc26fea-2a3a-3db1-8da9-94ba285903b0 | 3.05212 | -60.27966 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f572822-39ee-3b03-9ca1-f4b547aef851 | 4.08882 | -59.88913 | 2026-02-28 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55212917-005c-3a76-9bcc-aa4d02984da1 | 3.04432 | -60.28096 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cf72d35-a541-3743-a41f-d492304ab64f | 3.05524 | -60.27406 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d413967-bc18-3079-b6a4-350191f34ca9 | 3.1493 | -59.90724 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 77152331-d0d5-3f83-9458-5d5e3fea9292 | 4.80343 | -60.16806 | 2026-02-28 05:46:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14d83ccc-49c6-322a-b869-f935bd46527e | 3.04933 | -60.28353 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76a14df4-17c8-3e05-9279-ff24f70e0045 | 3.36947 | -60.62117 | 2026-02-28 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c0857a1-e07d-330f-b5a9-b2d1b31cf55b | 3.37936 | -60.60992 | 2026-02-28 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7166986-5f2a-3447-b177-685e0eeecf3d | 4.43596 | -60.75777 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66392dcf-80b5-3306-a3b4-7ddb9fe268ac | 4.27522 | -61.32729 | 2026-02-28 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36e1c9eb-e7d3-3185-8d5f-480a4bb02d99 | 3.0555 | -60.27236 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 367d178d-0268-3f1f-9698-091e98a98c93 | 3.15728 | -59.90595 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bcf9f9b-b3c8-3c63-bf68-d6cfeb17d20e | 3.05242 | -60.27794 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f44808a3-46e4-3ff2-8c7f-fa837ccf5961 | 3.37556 | -60.61054 | 2026-02-28 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6490b9b3-421c-3295-a5a6-3087a33db3ae | 3.05134 | -60.27471 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1af7e045-a423-366b-8caf-ad8850057f13 | 3.42607 | -59.87007 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6d4ef76-96da-32a6-bde8-9981f973b696 | 3.0573 | -60.01101 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 638c8bbe-2cb3-3eee-9880-7e57ceab6bd5 | 3.25431 | -61.28035 | 2026-02-28 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86bd9e0b-74b8-38c3-84fa-c8fd49641997 | 4.43291 | -60.76252 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec72f828-5bae-355c-9dd9-6c971dc7b104 | 4.27883 | -61.32669 | 2026-02-28 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dcacaa7-ad0a-3644-b63a-09385a586220 | 4.52811 | -60.98508 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b3e52d3-c0f8-38ee-b039-cb24aa1e6b3b | 3.15672 | -59.90248 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f54e1982-d0dc-3aa6-b39d-faf1a237365b | 3.4283 | -59.86908 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afacf910-2b72-398e-942c-e48a813368a9 | 4.44431 | -60.7496 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa7038d5-74d4-34fa-af92-a3a889a2573b | 3.37252 | -60.61586 | 2026-02-28 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7217a920-f4c9-3f67-9af6-7013148c4abf | 3.37259 | -60.54354 | 2026-02-28 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d99d0a5-e4bf-3490-bf88-37db817ac648 | 4.80264 | -60.16328 | 2026-02-28 05:46:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ece79c4-7b47-3e9e-8994-88aabdece1b5 | 4.43834 | -60.75959 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f79c9e0d-845c-3312-ad8a-a186b27a64a1 | 3.15329 | -59.90659 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13efbdf1-bcf9-389b-bfcd-9a1203e6c440 | 3.36872 | -60.61649 | 2026-02-28 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15327bf6-b9b4-3827-8df3-ff17ae9b65f5 | 3.15385 | -59.91005 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09687174-a05b-3c85-8241-26b3441515d8 | 3.04822 | -60.28031 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1716cce6-4a1e-38d0-9257-e590d4d74971 | 4.08886 | -59.89177 | 2026-02-28 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80ff3f46-217d-3980-b650-fa79e0bd0887 | 4.12815 | -61.06517 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3da730c-078c-349c-bae7-2b6173c12e10 | 4.43462 | -60.76014 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c681fdc6-16eb-31e3-a847-d555dda9dc7b | 3.47065 | -60.69342 | 2026-02-28 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa367789-db3d-34bc-9812-f88a619c35db | 4.43662 | -60.76196 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d337ea6-7f26-3f4d-9f9b-fbbec7120199 | 3.36954 | -60.54888 | 2026-02-28 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c125caac-4ff4-3ac7-9722-765326ab4790 | 4.44801 | -60.74887 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6eb87037-0b09-3b20-ab89-34c82a3a2448 | 4.43223 | -60.75827 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3894fe26-34d9-3418-bd4a-aac769c94081 | 3.06801 | -60.2754 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb47f578-1db7-36d7-8d43-dd0475e58c83 | 3.04937 | -60.0123 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbd2d3c9-9203-3487-82ee-c44cb1469519 | 4.43531 | -60.76435 | 2026-02-28 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d7c08aa-e0f0-3fa2-9fb4-f428a42309cd | 3.42489 | -59.87318 | 2026-02-28 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9530c717-02fd-3b65-b57c-a80fb90825eb | 1.47828 | -59.93359 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 810d12ad-25a4-3847-b65c-bff1b5ee0178 | 1.4942 | -59.93082 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a269190-3d17-3874-a548-19723e013b8c | 1.48664 | -59.93584 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f8e08c4-b0bc-3c09-89ce-1a6d4c4ce04f | 1.47589 | -59.94513 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd5f875a-22f9-347b-b440-2f50dfd5b5b9 | 1.46724 | -59.91641 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README5.md)
