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
| 4d25759a-3b4d-3820-88e0-1e6b6d5760af | -7.64034 | -43.58855 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c73f3adc-51ed-3ee0-ab01-360b7b5e67b6 | -12.15809 | -48.00736 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4468cfc-0c80-3288-9f79-afe60e1e135d | -14.12751 | -44.18407 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fab96f3-b042-3192-99b4-9c4c0ef314ff | -10.09281 | -36.2019 | 2025-10-31 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 5580071e-a1a9-38f5-9115-a6518f79f3a4 | -7.64778 | -43.58573 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe835196-6153-3c04-8d42-faac0049e192 | -9.98345 | -45.16381 | 2025-10-31 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 312ca96a-8d2f-37d9-a8c9-791e57164caa | -8.39347 | -41.84814 | 2025-10-31 04:08:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dfbadcc0-91e1-36c6-9d33-d3d6e94de288 | -10.4769 | -48.36097 | 2025-10-31 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e411dc9-ca39-393a-952b-e3437dd3db9e | -13.79774 | -47.06522 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3775d9e-9754-3c79-953b-3a5621935a2c | -7.62908 | -43.57146 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ac9187d-8bf5-320f-b27b-83e804e885bf | -14.20671 | -44.38694 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3803d15-4403-30d4-b44e-070612c9b99b | -9.88028 | -44.86686 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| caeced2f-9a7b-3c3c-a4c8-9e1d146dad2b | -13.32915 | -47.67933 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47586b5f-d53f-3ef1-b112-d0bf3f6b0e0d | -10.53522 | -44.78988 | 2025-10-31 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 35d644d8-26b0-32bc-8bab-edd54680d242 | -12.80525 | -43.48675 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3176a061-09ad-33b3-a4fc-b575e71e6f46 | -12.29174 | -43.19199 | 2025-10-31 04:08:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d802551-c979-3057-92f3-3a525c4a2285 | -7.92451 | -46.79348 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0da6eb49-ee28-3729-8de7-477984a57aec | -9.84077 | -44.14868 | 2025-10-31 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7879c48e-667c-39f8-8553-f455868a9a3d | -13.2482 | -54.35673 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9a90b1ea-4c8a-3b43-b6ce-645d3c397e50 | -12.93337 | -47.93152 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a5898be7-654a-331a-a20e-dacbdcd3c754 | -12.52688 | -43.75819 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| caff500c-0708-3648-856d-1fb3dc54c3ca | -10.53599 | -45.0456 | 2025-10-31 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b23f9fd-7344-3885-a9d5-43fa6415fb46 | -13.82612 | -47.06346 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2bdc6e5-7ce1-3c5e-b4c9-cdd5cc97fb19 | -7.34233 | -47.6316 | 2025-10-31 04:08:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e99891b7-24b0-3f85-9d8b-35c624350148 | -6.22182 | -52.0053 | 2025-10-31 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9065df37-9424-3e4e-857f-c6068488e5a6 | -9.73123 | -48.03046 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b44e9d95-ca54-3b37-8f3f-e2be59fc12f8 | -11.5569 | -47.07462 | 2025-10-31 04:08:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 547ea06b-72c4-33ed-bbae-d47bf2aed519 | -14.74292 | -42.46016 | 2025-10-31 04:08:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 78a93399-661e-3533-a53f-0852656888ed | -13.68263 | -44.71712 | 2025-10-31 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3324135-17f4-39f0-be56-4868fde241a3 | -9.51064 | -47.26708 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 173e74e1-d9ea-3543-9edb-72ab02f1c733 | -12.84398 | -43.47864 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f71b20bf-0095-392f-8c1f-182951c474aa | -9.71251 | -43.38051 | 2025-10-31 04:08:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fa5544ab-99f7-34a9-91ab-b4c937626f76 | -8.09923 | -45.17788 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6658bf4-1a0e-32e2-9ddd-a21248813cae | -13.684 | -44.53189 | 2025-10-31 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f8ee00d-ee92-3c6f-91d3-c20733d82f2e | -10.52795 | -53.71145 | 2025-10-31 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 73887f1a-caa3-34be-8d59-32f0ab516841 | -11.77659 | -40.90699 | 2025-10-31 04:08:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e66f4845-f339-38df-add1-925bbda08c33 | -10.92853 | -44.1693 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10d1256d-baa8-374a-be36-2bc6b47999bb | -9.72777 | -48.02626 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf6dafdc-35ab-3343-93b8-4c3edc1ea4c5 | -13.3252 | -47.67896 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 842d736e-04f8-3662-92e7-7bcbecd391e6 | -12.53406 | -47.54637 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88dacc1c-ff2c-3bd2-89d5-3365a83c8f03 | -7.65654 | -43.59841 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 09986968-ca7e-3d74-90f6-f76881c4475a | -7.60794 | -46.47572 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a8cec39-ff4a-37b7-89a8-96a9c33799f0 | -8.07309 | -46.80156 | 2025-10-31 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d9b878d-a71b-3d62-b3ce-c5dffba5e323 | -11.55775 | -47.06973 | 2025-10-31 04:08:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b6e4dceb-c687-39cb-bab7-0dbbfd0d9f8c | -8.55338 | -47.78655 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58aed761-6fad-387c-8647-652ebf876d57 | -8.09106 | -45.1371 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 449bffed-bc3b-3c82-aa9c-ef61bcf98cd5 | -8.94777 | -40.86707 | 2025-10-31 04:08:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e8218368-bef0-34b7-9003-e828c07de771 | -10.52704 | -53.71606 | 2025-10-31 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9336b43-2def-3c71-8cdf-74539302b307 | -7.67136 | -43.59345 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86657ebb-fdc2-38de-8752-eb50e4147ef2 | -10.9293 | -44.16896 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0d6d8182-1343-3670-b9aa-cc9b2fe17909 | -7.6179 | -46.47068 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bcbac79b-9078-3da1-baa7-62a3d1a058d7 | -7.95019 | -46.71503 | 2025-10-31 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86134fe6-31be-38c6-b369-76447b0eb910 | -10.74887 | -44.72836 | 2025-10-31 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a3d9594d-4ae7-3693-bd2c-25f337d72625 | -10.54127 | -48.71112 | 2025-10-31 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d8732a3e-b4bc-3eda-bde8-9fccc8fd617e | -14.16302 | -44.34621 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34d10ba7-b2dc-32dc-b16f-25d58b948da9 | -9.85988 | -44.8593 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0fbb5371-571d-33be-aff2-e9a4188cbae5 | -14.16584 | -44.34262 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a76ec9cb-bd23-308d-bba7-ef8bf4edcf05 | -12.28466 | -48.07179 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84fb7cc3-6c33-3950-8e37-21481083dde2 | -10.5387 | -44.79047 | 2025-10-31 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7c4b0313-ac0f-38db-816e-733ac1f5fa17 | -13.82238 | -47.06282 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 085bfec4-8289-3fdc-a4d0-b5b37d913782 | -13.62794 | -47.58778 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7444eb9c-9c66-3474-b90c-aa5096af1618 | -7.66335 | -43.59961 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 790bcee7-5eb1-36fa-bd3f-4e61b035fb92 | -7.77278 | -46.47922 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cc47ad9-2da6-3c2c-b479-95b4d5a33de6 | -12.29012 | -48.06454 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d26ab55-cb6e-3a5f-8a53-d930399a6ee0 | -9.50134 | -47.27284 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71c35c9a-deae-3251-b553-36110fe41635 | -10.58272 | -40.51386 | 2025-10-31 04:08:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d6c134a-c309-3695-9fd7-cf1d6cb94d9d | -13.53367 | -47.42641 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 021f6661-71d8-3d59-82e9-ab0ac11a645f | -7.81867 | -46.39833 | 2025-10-31 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2192b7e3-bf54-3fae-b6a1-cadfae3e259c | -11.03288 | -44.20144 | 2025-10-31 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4e0bae2-6206-307a-ba6a-6c09a571160d | -10.81435 | -47.58586 | 2025-10-31 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f9fe894-1b58-3b8d-9aa7-dbf05fd32ee9 | -9.88779 | -47.45597 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 947d4c30-a342-39e9-a56b-d87561e7f45a | -7.61395 | -46.47001 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e17cbf75-0852-3488-a24e-74aec719f1ed | -13.6723 | -47.2076 | 2025-10-31 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d4b3d68-1eba-39f4-a36d-a43b46b0a28f | -10.93022 | -44.76268 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8056e084-f500-36df-afc6-2f7f09f09256 | -9.51932 | -47.26486 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c75e87e6-e956-36df-8c02-595e8df11106 | -10.64429 | -45.24379 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d294feca-d8b5-3435-a326-018aed48e433 | -7.86421 | -48.88585 | 2025-10-31 04:08:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40a15f6a-0a23-3bbb-91c2-b2acc63fce3c | -13.80848 | -47.04744 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c0f43eda-548a-3503-bf54-764d49d926b9 | -14.51529 | -44.22314 | 2025-10-31 04:08:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b75ccf51-9a64-3742-9f7f-f21db694be9c | -12.1309 | -47.15425 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b0b213f-3896-3304-a557-ad25d951b8b1 | -13.98426 | -44.04164 | 2025-10-31 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01fe8c59-10c4-3f0f-b4e0-4d9bbcf963e5 | -9.85703 | -44.85473 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 22681925-99c1-3f91-94fb-502392716e81 | -12.28111 | -48.04451 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc4da251-bcfc-3929-8ce1-1ad6c00b3576 | -8.92301 | -37.28547 | 2025-10-31 04:08:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4760371c-1141-3bcd-93d9-b536e32c847a | -10.88561 | -44.32635 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dde415d-08fc-33c2-bfa4-7602cfd9637d | -10.93391 | -44.16214 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7f9c3051-f647-3d47-a9a4-29799cfaed06 | -10.93052 | -44.16157 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 155dbd2a-b55f-3318-bcbd-e16da1486eeb | -7.81168 | -46.39194 | 2025-10-31 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 16b4096b-5828-36f2-8b52-c86351390a5d | -13.81864 | -47.06216 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b25d796-e935-3343-acb0-a95739da055a | -12.52355 | -43.75764 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab78ee13-0c44-3391-b779-20b1af6199aa | -9.52274 | -47.26921 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cdb0cbce-938c-33b2-84c9-b7c5185c2348 | -12.60641 | -43.20003 | 2025-10-31 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8a7f078-0816-33a9-9853-d7d0d671f6a9 | -10.65463 | -45.20417 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2c048db-53af-333f-8302-ccf3a90f6a45 | -8.55928 | -40.74092 | 2025-10-31 04:08:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea22aaad-a90e-3f85-9414-b74f89f4ca1c | -10.53935 | -44.78656 | 2025-10-31 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f03dc87b-34f7-3b89-85b3-42857b7499ff | -12.53383 | -47.5497 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 701a1a0e-74c2-30f8-a04e-a684ed94a90a | -11.50314 | -43.25763 | 2025-10-31 04:08:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62aecfe1-bc71-34bd-939c-1410d2cc6177 | -7.65776 | -43.59097 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 6e2966f5-186c-3f0d-a0de-8fdafbf16bbc | -7.30771 | -45.66513 | 2025-10-31 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d9db905-6a40-3b17-be64-63d68711c611 | -12.8435 | -43.46038 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README24.md)
