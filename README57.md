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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fd9c045-d35d-345c-9413-e0edba73bcb5 | -5.87199 | -53.4986 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 878eba6f-0429-37bd-a597-2ac4919d03b4 | -4.27479 | -50.75596 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dccd103-9e81-3609-b8ee-2482de9991a7 | -6.0079 | -53.54439 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7dbdb5f4-1357-3642-8660-f10b99e151a6 | -7.34281 | -55.58082 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3228371-691c-3373-ad73-86b81e01e194 | -6.5033 | -55.89209 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6da034a8-6b37-3114-aea4-d95fe7ee65be | -4.26508 | -50.77151 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fa35a4b-d601-3a7a-9f50-d0b21285ddc4 | -7.19195 | -52.60906 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 814d8c29-66ad-33d0-a709-43f3460d1cdb | -8.2009 | -54.70927 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f73deb8-90c2-3075-bd2c-11bd6887977d | -3.00914 | -53.88224 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 21b90c6c-0f31-32a2-b83a-21fdb49109d0 | -4.2837 | -50.77015 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cd0ec38-b527-3bde-bc23-c56df0a8aeec | -1.64226 | -55.13058 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bbc7daa-1d07-3934-a4bb-b0d4662ab8ec | -7.51516 | -47.33464 | 2026-10-02 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c17c6198-32c2-334b-b792-66c9f31a0d1f | -3.81965 | -55.90817 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90050805-9b75-3512-a71b-697c6e553449 | -7.87275 | -44.18387 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 552b5af8-6632-3387-bb6f-b109cbb08b92 | -8.15559 | -54.82627 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be979bb7-5a9a-331f-b93a-337fddce23e7 | -8.02531 | -47.46902 | 2026-10-02 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe78e07b-c677-3387-87f3-97725f3fb871 | -8.23577 | -54.77219 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78900b77-e269-3680-baaa-92faedc8c980 | -6.39823 | -56.41259 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 151e9846-3f7b-3fe4-8e01-ff93048f89bb | -2.95766 | -54.09933 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00216c63-4c16-3623-9977-87b6e59d7018 | -3.11744 | -50.28379 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cc92e51-7181-3018-92bd-10e2adfa6f39 | -4.27243 | -50.74709 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f195f0a-5c75-3ad4-9807-268b7e0fdc41 | -4.45387 | -54.91045 | 2026-10-02 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3ebb321-7d3f-377f-9bcb-42552add1864 | -8.23907 | -54.77271 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58a937d0-1e0c-3978-8545-4bf9cb4acc8e | -3.22681 | -54.31504 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e55e22a-5beb-3281-a657-69feb6c4c380 | -5.75342 | -55.74799 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d21bde7-665a-3207-9fa6-84772bbd4697 | -3.10752 | -50.29964 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92afd9b0-9f95-335d-8192-a525aa5517a4 | -4.26945 | -50.74242 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c08fa18-4fe9-383a-a971-d39300057158 | -7.15162 | -55.13113 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c08ca19c-e428-3c8b-befd-e73407b178c9 | -6.22726 | -55.61728 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22a7bb40-33bd-3f9c-9af1-7697364137e4 | -3.10519 | -50.29061 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb5f92b4-f058-3b63-bb4b-3a9ff3e65295 | -2.90331 | -54.14386 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81fd2c50-89a9-3083-829f-79ea5c5e5751 | -3.14339 | -53.74208 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dadd27c-547e-374e-827e-cdac117d7b14 | -6.15206 | -52.80548 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d01e6b2a-9dbd-36a5-a758-6f3693a8fda2 | -6.15309 | -55.44233 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fff4f11-3624-30be-9488-d6929476d9c6 | -3.13902 | -53.74843 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5991ba8d-bd27-3341-86f6-4f8ac4e0f9e2 | -7.19423 | -52.61701 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7601e02-04f6-33fd-99f6-71ea72ba964c | -6.40018 | -55.23644 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2e031eb-4d42-329d-93d6-d8fe3b879910 | -7.49795 | -54.98374 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 301dcc02-627e-3f7b-8c7a-bbd9afa717f4 | -4.04116 | -54.22444 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2bedc12-444b-3257-a107-320ea3d90fb4 | -5.86196 | -53.47569 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a805435a-253c-3c4c-ad24-4186f2b7c1c3 | -8.17588 | -54.80463 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ede02508-ff32-3243-9f46-9588e39ad21e | -7.18796 | -52.61226 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1745b0f6-e68c-3bcf-82b5-85a2fb2b3909 | -4.42887 | -54.85285 | 2026-10-02 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a2ad67a-d686-32e3-b584-ed0f34249bb4 | -3.00254 | -53.88123 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d91c70fe-cd99-3f94-afc5-22e2dd224b8f | -6.4106 | -56.40246 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0099b732-fb0f-31b3-9ef6-a82e204a2990 | -7.34946 | -55.58187 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7656328d-de1c-3189-ab33-3a64299a8987 | -3.28346 | -53.84468 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 135e41e4-d4a7-3965-8a39-ddbd2e476764 | -2.21971 | -50.62343 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6a3758e-4853-39d3-812d-9d7d42d504e6 | -7.49903 | -54.97683 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d6f6fef-c2bf-3215-9881-424137a65665 | -4.35872 | -47.77098 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14fa0170-f2ac-3338-8354-dfc3df344337 | -5.16766 | -55.99943 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7379f00-6abf-3758-bfba-a152b60040c8 | -7.55144 | -55.0354 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a319b53-03fb-3d76-bf40-e967c62c84b7 | -5.86421 | -53.48313 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1a2ac90-25e6-3564-ae9e-c0d864409967 | -3.8533 | -55.80655 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54b08d3d-3b1d-38db-996c-c8385664af73 | -3.61128 | -55.51285 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 400d3c73-2cfe-3f52-841f-37ce6e27b8c4 | -7.5648 | -55.12281 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| facdec86-dc76-3269-abc2-1e3eac26735c | -3.13296 | -53.74398 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| af609088-8e70-3d6f-a45d-13b767b9af82 | -7.83818 | -55.11683 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d7ef6bb-f35e-3264-8fa9-a56b0a44db17 | -5.75938 | -45.14201 | 2026-10-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afdd20e2-677a-311c-9fe2-633227d0d9e0 | -5.98628 | -55.37916 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89730730-57ea-305b-a86d-4e4da949b48b | -7.52693 | -50.53567 | 2026-10-02 04:57:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5a87bca-c457-3ef8-94ae-8b6850e9592c | -6.71624 | -44.27995 | 2026-10-02 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0bd7da27-58f3-35e5-bf14-c287208134fd | -2.91978 | -46.72514 | 2026-10-02 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55a9f79b-e457-3b8f-8832-a6475ea3a1b5 | -7.17829 | -52.62984 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c122ead-8a45-3ce1-b147-5233aa45fec7 | -7.82664 | -55.12568 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67f632d2-6b69-38ff-b4e2-d952c279502d | -5.13999 | -49.87084 | 2026-10-02 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 060e2057-94c8-30f9-afbe-776577345e72 | -7.04906 | -55.63157 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 59766498-80b4-3e69-b661-9ec9273961c6 | -6.38965 | -55.23841 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 089c8208-643a-3049-a1dc-a6a87d15776f | -6.34537 | -55.32472 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9991327-ae89-306b-a1be-9af92533a3cd | -7.28487 | -55.60403 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1b3004a-db59-3d29-8be3-4d8e9c0560d4 | -3.01126 | -53.23619 | 2026-10-02 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee563fc2-3322-3685-a400-8616ee864a49 | -3.12064 | -50.26505 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8ca42e7-04f5-341b-b7e3-fcade0281ff4 | -2.11062 | -48.99961 | 2026-10-02 04:57:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fa18317-4f46-3565-80b3-f34949898530 | -3.62998 | -51.93262 | 2026-10-02 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f51426f6-070e-3b46-89ed-7ac4ed5b988a | -3.22735 | -54.31159 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c813a40e-9921-36d1-8740-e53cadd90d00 | -7.82443 | -55.11822 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fb91b5c-84f8-3fb3-8264-70a9035a3879 | -6.2462 | -53.14616 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e746d63d-2d03-3102-b6d3-b54676b01b44 | -3.00692 | -53.87487 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a76dad0-0200-307e-a9a3-5eefe8d959e0 | -4.29325 | -50.78006 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 155ca486-b3de-3154-9007-5e0eaecb7f82 | -1.25832 | -54.56244 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ea4b617-e0f2-3c5d-ad28-b4a9d4148600 | -3.28845 | -53.85599 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63709df6-472b-3a3d-9d1a-f5caf01c8ff6 | -7.49632 | -54.99412 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf5dc00d-f708-3572-b207-cdc100e4a81e | -4.2693 | -50.768 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f423c748-0146-33ef-92cf-48e56878f078 | -7.54814 | -55.03488 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4522f5b-7347-3236-8ce4-2bcfc08f5593 | -3.97955 | -41.52229 | 2026-10-02 04:57:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a339f95c-4216-3755-b84f-a741d22fa135 | -7.71463 | -54.75285 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff32255e-93f8-3b63-910f-2a4db793c362 | -3.86523 | -55.81977 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44b6487d-fcd7-3bef-bbae-5e2a275c1ad9 | -4.27227 | -50.77272 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c1c3e0f-c0b7-369c-a5fc-65b5b23c7150 | -1.81803 | -57.1053 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad0d84a1-daad-3a44-9052-1cd2db6afa16 | -1.63431 | -55.13685 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b1c281a-d9da-343f-8a5d-27c481b94df4 | -5.01049 | -56.28474 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1867122f-2d65-3e75-b651-5d7da1541e9c | -6.20198 | -52.9422 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb7751f7-4753-3a4a-ae73-a4b5f5bad442 | -3.29611 | -53.85014 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 33c97732-ee2c-3729-8ac8-04fc7f4efb9c | -6.84603 | -55.53811 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38e013f0-c000-3697-bf27-98fed00adcf2 | -7.59843 | -55.6869 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7f82f00-9902-3289-a16c-a7e19b68ff34 | -2.05089 | -56.86225 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 6d054633-a2ba-38e6-aaea-1061348da6f2 | -3.10585 | -50.28635 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b961c14-63ea-3c75-976a-62e1a3b7f0a5 | -3.17277 | -54.09457 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68adb9dd-09ee-36dd-a311-1b7e3d1f94d4 | -5.11863 | -56.02222 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c591ad0-0b88-3729-a623-df1fc2909471 | -6.39599 | -56.40459 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README58.md)
