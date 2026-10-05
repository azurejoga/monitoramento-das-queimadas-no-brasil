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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea60f523-821c-387e-9289-c6457c600a50 | -3.37948 | -54.10804 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06665961-db70-396e-aed0-6d426cc7537d | -2.87034 | -54.11352 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30c1555d-afcb-3cc2-80da-00cf07257311 | -3.11977 | -53.75758 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 950e54de-6c4d-38e5-8586-592964f735bd | -6.25895 | -52.86319 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e1c5d9e-63b4-35eb-ae0b-02336b4a2eb7 | -1.88359 | -56.28601 | 2026-10-05 04:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7ed89262-3200-3562-89c7-46fa9bed6450 | -7.11851 | -55.72264 | 2026-10-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 663950cc-d2a6-35d6-a12f-891d4e736942 | -3.04117 | -54.22806 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0ef14bf-659f-37f2-bab3-7a631f4ec968 | -3.11695 | -53.7534 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9240b98d-7eb3-353d-a48c-2f07c6b5a32b | -4.1221 | -54.02617 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13ca6af8-ab94-3ed0-b81b-8dd87e273e44 | -3.77496 | -51.40503 | 2026-10-05 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f64d437-dce3-3964-9cec-35f9c1bf0ee6 | -2.96232 | -54.10811 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c33d22b8-1d23-3708-8b54-97f88a7785e5 | -2.91758 | -54.10097 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 312a6960-98ce-322b-94ba-798677e54678 | -2.94959 | -54.12149 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f37151d0-abd9-3f34-95fc-f2d04f1c161a | -6.19806 | -52.81868 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf9a61b8-a11e-3513-b8db-4140a3e58154 | -4.26363 | -50.73994 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2de8e6e3-19de-33ea-ba2b-022ef8e2463a | -2.80307 | -54.11439 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d8715ec-d8e5-37d1-9b53-2e5f9c4eb890 | -2.89875 | -54.08644 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdd24338-1ca1-317e-8ca7-50977349bdaf | -3.13575 | -53.72279 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c16044d3-3a2e-3ebd-822b-fa7aae47a21b | -7.47306 | -54.99529 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b13947b-8ebc-333e-8df6-43bce676c147 | -3.10114 | -53.74343 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a89d01ee-96cf-33d8-8ad8-8631c222f981 | -3.28486 | -54.17379 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 708fc809-cf80-31a4-a47b-7d18f4737938 | -3.50448 | -54.61706 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1108cd7-6c22-36da-acfa-6c6e06451c5d | -3.14905 | -50.43231 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 223b051a-3dc9-3926-8d05-326a137d1015 | -3.33331 | -53.39305 | 2026-10-05 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0f5a62a7-3336-3793-b322-7f74bcfe1821 | -2.94042 | -54.2011 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 505e16c8-fd6a-34e4-bbd6-11ac8e84dab0 | -5.5842 | -49.74603 | 2026-10-05 04:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1003d915-f63e-37bf-afab-667a720f2915 | -7.44005 | -63.56138 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eefbf18d-24b0-3f66-8815-0a48637aa97d | -8.87106 | -66.65073 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41937233-7e46-3c2d-b15f-1bcc63cf4a57 | -16.67529 | -41.85227 | 2026-10-05 04:59:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| a4e8db4e-8cb8-3bb5-b8f5-c2a90445d210 | -10.96908 | -45.4295 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 556cc7c7-a79e-3b4b-8fa8-4d2756c80291 | -8.34437 | -62.8288 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 48f835a7-1208-317b-a891-4715fd9c2bc6 | -12.88404 | -61.71427 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d15a18db-b3d7-3488-be73-8f38ad09d17c | -9.09225 | -64.38729 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c01f75fa-5595-3904-be11-9bcfb0d7b926 | -11.97234 | -63.61242 | 2026-10-05 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de428304-0560-345a-87aa-bebd434e8ea2 | -8.33894 | -62.82773 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7a1f722-6ddd-35f6-a946-d8ac3cc88ccd | -10.53462 | -48.06515 | 2026-10-05 04:59:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a345a42-07b9-3c00-a6ba-c1da2d211c30 | -8.34311 | -62.82982 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7ab0558-6811-35c4-a138-d5d8d24cde03 | -12.87649 | -61.71531 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54833301-266a-3eb3-8440-61e9d249ad1d | -8.74115 | -64.19254 | 2026-10-05 04:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ff2d7e8-a4f9-3c4f-aa5a-292113c66144 | -9.66973 | -66.83443 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2406b5c-85e7-3fcc-968d-4d3165db8838 | -14.30069 | -57.46862 | 2026-10-05 04:59:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e097869-cbde-3532-8efe-006e73cd1876 | -12.87753 | -61.7234 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0e758af-1a88-3b18-9343-ca14be9e2217 | -9.15663 | -63.16534 | 2026-10-05 04:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0831143b-8913-3ba9-bb81-52454bb6bf5b | -12.88115 | -61.71622 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb50d478-9af3-363f-a910-cdb6432706bd | -11.6794 | -43.64062 | 2026-10-05 04:59:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ca4b8354-40ea-39c6-b91d-a22332fd9e1d | -10.96398 | -45.42917 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efa730a2-394c-3695-a5cf-d54d39c27d0c | -9.10904 | -64.36341 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c73af77c-6cb0-3eb3-98ce-802d9eb16fc9 | -8.35653 | -62.81771 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56bb1544-c4ea-3e09-af82-af4c2216a9fd | -10.96596 | -45.41416 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8d8de59-1cf0-33e3-b58b-575da5488e61 | -8.87783 | -66.65228 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4137c5f-16fb-3df2-b5e6-3c67234c29f2 | -8.33704 | -62.86792 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbb7062e-5393-3aa0-a766-671db8a20180 | -10.87488 | -61.40927 | 2026-10-05 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a47fe3e-9e48-3941-b1ee-e549f12ea8ce | -8.34915 | -62.83339 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c806a4e-c82b-3d12-a454-a89d1b65ca74 | -8.74035 | -64.19688 | 2026-10-05 04:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a04f4011-8858-36e8-b683-c7cf5f997b0e | -8.35856 | -62.81314 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e6df6b3-0aad-37b1-8763-4c6ce72b3a7c | -8.34848 | -62.83693 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ba7c104-c36d-3004-9e0b-be370495a51a | -16.67416 | -41.84925 | 2026-10-05 04:59:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d5c06480-12f3-3cdc-94f5-2e6981ac2389 | -10.95408 | -45.42622 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bfa72c6-4345-383d-b7cc-76040ed82a34 | -10.87468 | -61.40752 | 2026-10-05 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa2a3447-34a6-313f-98bd-2453ea8cb656 | -11.97167 | -63.61592 | 2026-10-05 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea07deb1-8c8b-3366-b57c-fb5ab9f7b267 | -9.12818 | -65.91724 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4309609e-e6b2-3d51-831d-b49e30a82428 | -14.4272 | -59.88079 | 2026-10-05 04:59:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40a5b814-29bb-38a8-86bd-5e6d898be882 | -8.84367 | -62.85941 | 2026-10-05 04:59:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8e51a09-dc54-3edb-9ae1-b4d2db869635 | -16.67361 | -41.85501 | 2026-10-05 04:59:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ad574969-a982-3f01-9f87-5505270695ca | -9.12169 | -65.91592 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f74fb7e-a4d0-3ac4-9cb0-ddd17fce2349 | -12.87553 | -61.72032 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 240cac33-0a63-3af9-a1a0-06875ff41e33 | -11.68459 | -43.64602 | 2026-10-05 04:59:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7e08da4-2c1e-301c-8fa4-2b89d65981a6 | -9.40042 | -65.895 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 500aac9e-e229-3a29-99b4-0d8fbcde77dd | -12.87845 | -61.71837 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c94b911-9b13-3dd1-b804-e301f41b7abc | -12.88312 | -61.71931 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4de892e5-d0cd-30f5-afce-dbb0ee462fde | -13.50246 | -61.12434 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 659a26f6-8e03-38d7-9c38-e7dfcefa932d | -16.67582 | -41.84645 | 2026-10-05 04:59:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 8c5cbb2d-3122-3284-83be-7bf3afdeeb70 | -10.96359 | -45.43213 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d88444d0-36bb-3f1a-b198-4643a976d83c | -10.95444 | -60.909 | 2026-10-05 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c66e2fe-dfa7-31cd-a08e-e8b2cbe167cc | -12.88019 | -61.72124 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04669cab-f170-399e-8faf-bfa96da38735 | -9.12927 | -65.91162 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f2c2ad5-219a-3130-bc08-626a7890c626 | -9.15114 | -63.16431 | 2026-10-05 04:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2468e6b4-4f5d-3bf0-8ae7-e1313ad018eb | -9.15107 | -63.16394 | 2026-10-05 04:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c86c6556-2aa7-30c5-b02d-a536fcf86393 | -9.02738 | -67.55668 | 2026-10-05 04:59:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8bcd0fb3-5ef4-3ff0-8191-cd64d7af97f1 | -9.09309 | -64.38285 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d1dfb4a-0735-3216-86cf-492a52d7886b | -10.83013 | -61.40983 | 2026-10-05 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d84803f0-64b3-30f0-a7c8-7984dcc6b7c9 | -8.34855 | -62.83088 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03edce4d-aa8f-3856-a83c-d568b15e0c92 | -8.34663 | -62.84154 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85fca5bf-51ba-31c0-8897-c2b60ca2ec9c | -8.34247 | -62.83337 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7acb5d1f-af96-384a-b74c-e927d520a638 | -10.95532 | -45.41679 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0adbf518-ce57-336d-9032-4f9e53ff2d60 | -8.35272 | -62.83902 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1d3a515-7fd9-3710-ba12-1b5e3b190b60 | -11.6789 | -43.64474 | 2026-10-05 04:59:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a05bca0-7b77-312f-9cec-3e50ee0b47c5 | -8.35716 | -62.81417 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a12538d-58d8-3863-b8e2-9411db28896f | -12.87457 | -61.72534 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 285219fe-3124-329d-9022-9758c96cfc7b | -10.9683 | -45.43542 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d460a8d4-f128-397f-86eb-a30e36ce1bea | -11.68509 | -43.64191 | 2026-10-05 04:59:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97a78c81-c3a5-30f5-aa4d-848e09932d0e | -9.39932 | -65.90244 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba617dc5-2e31-37e9-bdb7-1f22b8c25977 | -8.34371 | -62.83235 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74c71680-9f18-3bc1-b374-c3380c7fdde9 | -10.87942 | -61.40841 | 2026-10-05 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e11d68a7-5e4e-35c4-9b0a-e19e11440fad | -9.15656 | -63.16497 | 2026-10-05 04:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc8c7bb0-127f-3003-840f-f4990ef9468a | -9.39934 | -65.90048 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1161f54-ad0b-3631-9a39-5ccfe8a8183d | -8.34375 | -62.82626 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65298abb-68e5-3eec-bcb6-72958af6930c | -11.68413 | -43.6498 | 2026-10-05 04:59:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 648186ac-9e73-346d-9e82-ef6dff5d2dfb | -13.73405 | -48.48135 | 2026-10-05 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8775d1c-8254-3962-b663-02b657e51a3d | -13.29585 | -48.37747 | 2026-10-05 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README48.md)
