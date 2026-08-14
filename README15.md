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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 944b9815-8496-3466-a441-713850399701 | -14.47236 | -45.69529 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9141c1bb-0fe6-37e9-8eb4-7bccd4eb2482 | -12.49648 | -43.77511 | 2026-08-14 04:14:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 13b6e677-a742-351a-84ce-3f524790becb | -14.4524 | -45.69404 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e410e8ca-c71c-3614-ba36-157a10b83a96 | -14.45162 | -45.69857 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d72e1988-a4f3-334b-b2fc-6f41fd4d6f4d | -12.73572 | -48.43757 | 2026-08-14 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61417cf1-c4ed-3834-bde9-cb0c558f13b0 | -13.38754 | -42.38659 | 2026-08-14 04:14:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c7226310-d58d-3c5e-b688-ecf21ade053d | -12.51598 | -55.79612 | 2026-08-14 04:14:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9506611a-63e0-3ebc-be72-61b4819f4afc | -14.9438 | -46.62931 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bdff887e-2779-306b-9328-bd14faca09d6 | -14.29632 | -47.15201 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 564bd4ce-7269-3915-a1c7-c105d46f3d6c | -8.10852 | -42.56568 | 2026-08-14 04:14:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bff91fac-57c7-3b8f-aa2d-80edfc185f49 | -13.24394 | -54.2286 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad655026-8af5-3931-9893-ed99ca8b8ae9 | -11.49147 | -54.62234 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f5543c84-1e84-3a75-b1b4-1bb12b433126 | -13.27631 | -54.23047 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4f937bb7-0eb6-3534-bac2-5eaa7955e932 | -15.63426 | -42.39218 | 2026-08-14 04:14:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9c3eb9e-ff66-333c-931a-b28b9dd20c7a | -10.96974 | -50.54163 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcb94dfe-7c46-35a8-8881-02759d36c76a | -15.01091 | -41.94676 | 2026-08-14 04:14:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f7fd1e77-d836-3e09-b26f-2a5fb3d04062 | -14.94862 | -46.62472 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8020d323-f073-393d-a377-90fc2e1e5c7a | -13.27311 | -54.21824 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a545f2e-da60-3fd3-a42b-b7d8a9e59098 | -9.12502 | -46.39059 | 2026-08-14 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26a09820-85ae-3f90-9d06-8ccf6f4aad70 | -14.57397 | -46.76529 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f42fe493-d26a-3087-a919-491a085064c8 | -8.52295 | -45.33602 | 2026-08-14 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6fe40cb-fc36-3121-b68f-27e9b203c681 | -10.98584 | -50.54488 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e5e412c-6dd8-3d91-ae0d-5bcbd5579b9e | -11.48355 | -54.62552 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e48b49c-20fd-3ba8-a676-42833bbfe34c | -13.23447 | -54.27392 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 31e80db4-cf77-3012-8ff5-a85e03453cd8 | -11.48896 | -54.63362 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 78bc813d-c7e7-30a6-a34e-6c75de76ac7b | -13.24326 | -54.25831 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2fbb7e3-9ef2-358f-8657-1226d261f7cb | -12.51537 | -55.79063 | 2026-08-14 04:14:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17aa5315-bd22-3049-b506-557bbc935e9e | -14.72106 | -52.89765 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81a350e0-8fc0-3f92-b08a-b80a4945c567 | -14.28811 | -51.97339 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df2c7356-9979-3624-b05a-e70d4a7b3c82 | -20.99988 | -47.27557 | 2026-08-14 04:17:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99e43090-6cdc-3c18-97b0-147e60e310d6 | -19.87914 | -44.05162 | 2026-08-14 04:17:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8e1b0c40-44f3-34ac-aa27-b77366ddf9be | -14.03459 | -53.58917 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fedc9bc-db8c-315d-b112-4ca020929127 | -16.54349 | -39.66477 | 2026-08-14 04:17:00 | NPP-375D | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 31e921ef-7cdb-3f63-a1db-d4af59612062 | -14.72207 | -52.88709 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95eb92b5-b8ee-3c8e-b081-e3950f624bb1 | -14.32548 | -51.98851 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3414d3f-96b6-3f26-af76-0391c381c4df | -21.38652 | -48.63344 | 2026-08-14 04:17:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f751cf47-28a5-3adc-b399-0dd1541e5c80 | -14.08713 | -53.63601 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ef55195-2247-3f42-87a9-bdd5949beaad | -14.28965 | -51.96584 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8853bb20-9d16-3001-82a8-1ad806835182 | -21.59479 | -43.70087 | 2026-08-14 04:17:00 | NPP-375D | BIAS FORTES | MINAS GERAIS | Brasil | 3106804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 057c2cfb-279f-3b6d-b2b3-7f5feaec8eef | -14.32622 | -51.98485 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae7060d1-2e47-3963-8ed3-7c2eb4c2f98b | -18.69844 | -44.54855 | 2026-08-14 04:17:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87ee0357-4f98-345f-ac3d-8497bf6983ec | -18.48808 | -43.40219 | 2026-08-14 04:17:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 64b2b65a-0a7c-3bd0-ba0b-4b606e3f341d | -20.89499 | -50.508 | 2026-08-14 04:17:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9fc024b1-1597-3844-9ae7-b6c5c55144c1 | -21.45328 | -48.68332 | 2026-08-14 04:17:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cde9898-91e0-3ea1-9673-6019af90a8b8 | -14.35349 | -53.69222 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2a5cc03-a5ef-3bad-8ca6-901b8fdce04b | -14.33024 | -51.99357 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d185db8-61d7-3e2a-90ea-2f507ed6ff15 | -16.71924 | -46.40133 | 2026-08-14 04:17:00 | NPP-375D | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de2b01b4-d1b2-32b2-84f6-63db3b37ad28 | -20.39509 | -41.63245 | 2026-08-14 04:17:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bffbe143-bd66-3f42-b54b-3113e245fd8e | -16.87376 | -54.13221 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c983c2d-91ea-3ed6-a64c-2ac0e06b1319 | -14.45305 | -51.8618 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a52f304a-fc99-37c8-aa2a-8f4191ff440d | -14.33441 | -53.30399 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3206ee00-13b5-340d-a2d1-1d4b60b8eef9 | -18.49531 | -43.39979 | 2026-08-14 04:17:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3d5fa827-25f4-35a9-8185-6647189450f9 | -18.27936 | -42.82424 | 2026-08-14 04:17:00 | NPP-375D | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a23051a3-8784-37b2-b03a-b0f9c97b99a2 | -14.33947 | -53.30978 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 611f4795-ad82-3a88-90e9-2ca302690901 | -20.95938 | -47.20451 | 2026-08-14 04:17:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 046fb2d8-db25-3930-80fc-2864bd4a48ec | -16.9166 | -54.13857 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01097d23-6fcd-3bdc-9e92-69598d2c04d3 | -22.75983 | -47.07261 | 2026-08-14 04:17:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a7b6876-8ae2-3b4e-84f3-30470687ad50 | -14.4645 | -51.91868 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35578e6c-03ab-3a72-aebd-121df3a734fe | -21.73948 | -44.06673 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 955134df-85a5-3eea-a432-977c590adebb | -15.12464 | -48.65305 | 2026-08-14 04:17:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b965944c-d37d-3462-9ab4-0f726be7bb3a | -14.29043 | -51.96208 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 358de37b-4fd7-3294-9563-f685028e0df2 | -20.26182 | -46.70918 | 2026-08-14 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 75dadf68-2c4b-3bc7-8a6b-d3f5f4f07936 | -14.71543 | -52.8897 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdf22f0c-3a8d-373a-979f-03088eb3d855 | -19.04257 | -40.40429 | 2026-08-14 04:17:00 | NPP-375D | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| baec11f5-109e-398c-9b2b-3116a0d9c821 | -15.17202 | -50.0514 | 2026-08-14 04:17:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe55c267-8a99-3607-b458-e2cd9bbe1f90 | -21.74818 | -44.03385 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 46237a28-5181-3296-be60-0562c01ed312 | -16.91566 | -54.1429 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82070f58-9bbf-39b3-a958-f5d7684c339d | -14.04638 | -53.58558 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35a63c1e-ff68-3256-8162-8343dffd5f4d | -14.30153 | -51.96425 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78bd9d06-b10e-3ee7-8f5b-2f612db09709 | -13.82545 | -53.79521 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c044a4ae-5d30-3306-8a4b-2a14a24da355 | -15.63502 | -48.8974 | 2026-08-14 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d0919a4-6b21-3174-9c1e-436e276f7c7a | -17.74171 | -50.87749 | 2026-08-14 04:17:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c25d273f-2c29-3919-b817-0e80b3231d9e | -18.55245 | -48.18583 | 2026-08-14 04:17:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d71cb24-71dc-35da-9b45-e66dd6780bef | -18.54098 | -48.2026 | 2026-08-14 04:17:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50d23e03-c92f-3135-a9fb-031a4b69e31d | -21.123 | -48.92054 | 2026-08-14 04:17:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| af4aa7f5-8583-36c5-a4c3-797eb07387ee | -14.43583 | -51.8621 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f59c4cfa-495f-3eeb-8b7d-a71c001617e0 | -18.47804 | -51.74533 | 2026-08-14 04:17:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a986be9a-9777-3597-9cfc-4c45ae6fa0bf | -21.75211 | -44.03074 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f37ad727-d26f-345a-add4-3f669eb4fef8 | -18.29062 | -46.08072 | 2026-08-14 04:17:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 310f49dd-8edd-395b-88cb-2abf72010460 | -15.87452 | -43.06803 | 2026-08-14 04:17:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5d0cfc0-1e54-3fab-9698-51582b4822aa | -16.92046 | -54.14993 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2215934-cdae-3766-bbde-76c53e143f00 | -13.81804 | -53.79943 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9c17422-15fa-36f3-8628-3da17093a9ca | -13.92386 | -53.96407 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a677e412-f693-3494-8ca9-92590abb813b | -18.55571 | -43.56775 | 2026-08-14 04:17:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c6c75a38-4524-3b26-81d4-840047eda07e | -15.16719 | -50.05044 | 2026-08-14 04:17:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c07ba9e2-cecd-342f-ad2d-cf8c4c59aa48 | -15.33399 | -48.00823 | 2026-08-14 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27d22a92-4e07-3580-952c-34ed35fd6b3f | -21.76267 | -44.02884 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 403e298b-e88c-34d2-8a29-9d68ebe02672 | -18.17339 | -43.98229 | 2026-08-14 04:17:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f85c583f-4952-3baf-af97-47d8190d34e4 | -13.82429 | -53.8007 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69a4c485-8798-397b-b762-ab1d4eaefb4f | -18.41406 | -45.19571 | 2026-08-14 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4abbaf0-bcdd-3e24-a57f-4fa1a7115154 | -14.71616 | -52.89187 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53541b72-da27-3f59-b74e-76b6a0e84dd0 | -20.32355 | -42.01789 | 2026-08-14 04:17:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c5f695a2-28ca-32ab-be09-be2730dfed1c | -19.87161 | -43.24103 | 2026-08-14 04:17:00 | NPP-375D | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 894b2c77-adaf-3679-8b79-41c00e6336bc | -22.75626 | -47.0719 | 2026-08-14 04:17:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e3e4144-4e6f-351b-b818-739aaa1be6b4 | -14.29596 | -51.96324 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcf04002-aca9-3197-8d4c-827d46ebecb2 | -21.74546 | -44.02951 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 003e00e1-e440-3910-abfb-f72468008e70 | -18.5179 | -44.17867 | 2026-08-14 04:17:00 | NPP-375D | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd6aea5f-7548-34ab-8c71-2b1031465de7 | -18.54844 | -48.18497 | 2026-08-14 04:17:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64a89be7-4eda-3bd3-8f06-7315135f906a | -14.44681 | -51.86438 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fe0f9fb-75ab-3272-9f91-04504a39292e | -16.3448 | -42.8807 | 2026-08-14 04:17:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README16.md)
