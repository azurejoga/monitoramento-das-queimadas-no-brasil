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
| a2d109c2-4b90-3e0f-8d59-84acec8afce7 | -11.37775 | -48.92842 | 2025-11-01 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09ede41d-a060-311f-a444-8f426ea817ae | -12.91272 | -45.06619 | 2025-11-01 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb38e0e6-9681-3362-9b71-3f0f5efc56b0 | -13.1622 | -42.28239 | 2025-11-01 04:40:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7463de9f-85b2-335c-87b1-a0d2b28a3d3b | -13.70962 | -43.57411 | 2025-11-01 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbea9008-bd3b-337c-98f3-8cf4d416325e | -10.64111 | -42.31948 | 2025-11-01 04:40:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b7b1ff82-92ef-35bf-a6c8-ec1facbdf618 | -13.5294 | -47.10912 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb2c6bbc-8cee-34c9-b303-6f01a093c8f6 | -10.86835 | -47.55436 | 2025-11-01 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6618e261-5aee-3545-bdc6-2ac9cb6e64e9 | -13.0298 | -48.25797 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b84b31dd-b6e2-3516-9372-3896a026a651 | -13.78912 | -43.25325 | 2025-11-01 04:40:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8308cd0c-cf45-3237-99a6-d6535e515c4c | -12.61128 | -48.44207 | 2025-11-01 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2357c97-aca3-3cda-9820-8a4528dd7380 | -13.38031 | -54.28806 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6a8d5f4-cd00-3d92-b7e1-4545058a9814 | -11.74474 | -59.30725 | 2025-11-01 04:40:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55ff3390-7862-353f-841a-cfbddc926a20 | -13.94182 | -50.33765 | 2025-11-01 04:40:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 699bb982-fc0d-3fc8-ac1f-2a3fb828cb92 | -12.43783 | -43.69544 | 2025-11-01 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e8e0909-7de8-37ae-b34f-5dbd612cccda | -13.50954 | -47.11535 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bbb425e-a954-35d0-9473-ca1a6f6c037d | -12.90958 | -48.24069 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd38f86a-100a-30e4-8d71-25cef9daa830 | -13.37957 | -54.29235 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 478dd7e6-85e6-389b-b17e-bf4a276f71ad | -13.29193 | -41.93153 | 2025-11-01 04:40:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31871002-c40d-3cb4-92b4-e9b66ef5e0bc | -13.51016 | -47.11095 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25f603da-06ef-3b48-9ee6-18dafa5030e6 | -10.63147 | -52.1827 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 39860922-82e9-3408-9c86-416f74348e48 | -12.90666 | -48.23618 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9351c5f5-1d2e-3105-a42c-94f3ed896139 | -13.02689 | -48.25342 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| da0a4a9b-de38-3d5b-8a41-304e19cc5794 | -10.53866 | -53.71188 | 2025-11-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3540577c-9122-3381-8ae9-235b6c873a4f | -11.94466 | -43.34607 | 2025-11-01 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50e841ea-1672-34a3-98ca-7d3a75ea7caf | -13.32311 | -60.71363 | 2025-11-01 04:40:00 | NOAA-21 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2145a436-daa4-355f-9436-10a08a683cf4 | -11.73368 | -47.47062 | 2025-11-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 83fab0b1-bd0f-3970-a84b-9029bca569b2 | -13.74707 | -43.60065 | 2025-11-01 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0b6aa24-4025-33c7-8607-f2bd7280d638 | -12.02309 | -63.75142 | 2025-11-01 04:40:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4a25bc28-3b5b-33e9-afb0-ca680c06776a | -10.64451 | -52.18871 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdef1a2b-2e73-3109-8a18-7e7b611745ed | -13.13969 | -48.46851 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59ead035-d743-3a0a-b8b6-9050db71464e | -10.6411 | -52.18815 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00d8e954-9ed9-3cca-b783-7b683ae6d82d | -11.72937 | -59.30443 | 2025-11-01 04:40:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3ae56fe-5e2c-3c61-8a9c-0c9fcf5f8657 | -14.08349 | -44.15714 | 2025-11-01 04:40:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ef799f64-95a3-38c0-852b-cde496b690ca | -13.52135 | -47.11229 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83c8a31e-b942-3094-b045-684cb53d6e03 | -13.36942 | -54.28618 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc2bb093-a1d6-34b5-aaaf-457f6dd08f6a | -12.43741 | -43.69312 | 2025-11-01 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5b90af2-6d41-3b0c-8043-784271ff1072 | -13.20498 | -43.12915 | 2025-11-01 04:40:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e739c1d9-d3dd-3af2-bb28-f1daf544cba6 | -10.9008 | -47.50554 | 2025-11-01 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b3666c2-523f-38c8-9391-f1cb9269b1b2 | -12.88885 | -48.27454 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 777872c2-3028-3923-83f6-57755b33d10d | -11.58721 | -49.91005 | 2025-11-01 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2c5cce6-9d13-32e8-8a6d-8d6ac10456b1 | -13.51453 | -47.10678 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 060eefac-7633-3e05-8cfe-13651d9f9efd | -11.62417 | -48.48344 | 2025-11-01 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e41c73a8-cc31-397e-a1f9-3cb2a1605106 | -11.38168 | -48.9253 | 2025-11-01 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5647cfdf-b411-3070-9a72-5bed599331cd | -13.63358 | -43.1712 | 2025-11-01 04:40:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c7082444-ca09-32f2-828d-055337d61a41 | -11.64135 | -48.60157 | 2025-11-01 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c9f4226-e7b0-3228-a0a8-50ba8977f82a | -13.16037 | -42.28512 | 2025-11-01 04:40:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0aa25bce-6cd8-3ad3-8f89-077c9def1f33 | -12.59792 | -48.3405 | 2025-11-01 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0f70f8a-c77c-3fb1-871c-62d307bd1383 | -11.44176 | -48.17928 | 2025-11-01 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 254f07ce-4a97-3d90-8125-c63a02b8ca6e | -11.5839 | -49.90952 | 2025-11-01 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57b38536-8723-3764-994e-1ec0b1e6ce4c | -14.07682 | -44.27925 | 2025-11-01 04:40:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec86e079-69d6-38b7-a880-f5006afda422 | -12.02844 | -63.74503 | 2025-11-01 04:40:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 206a0886-aa0d-379c-8a56-5979a06d6895 | -12.88645 | -54.75488 | 2025-11-01 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e23a0447-b5d9-307b-982f-7dae24bc4568 | -11.66561 | -41.6864 | 2025-11-01 04:40:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa6dc34a-053f-34ae-bda7-d3afba1df3ec | -13.66556 | -47.20675 | 2025-11-01 04:40:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4c7c318-5f5e-3953-a03d-8d112ab3f8f2 | -11.64022 | -48.60905 | 2025-11-01 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fdd36d2-63ed-3dfd-b15c-bc6104cf0a78 | -12.178 | -53.66572 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb28ddad-abc0-36e8-9b91-5900a3291ac8 | -13.43868 | -44.42675 | 2025-11-01 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 450f3ef4-e9a4-3910-b314-1616bf73c3dd | -10.14952 | -43.92195 | 2025-11-01 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 115d12f3-1418-3da8-ab03-233cd098ea45 | -12.50604 | -49.63671 | 2025-11-01 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc5594e8-25ed-3d52-99ff-510cc18b2c38 | -13.65229 | -44.40601 | 2025-11-01 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e16c28f-6baa-328f-97d7-96a93fe08e98 | -10.64182 | -42.31399 | 2025-11-01 04:40:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5361f45a-3347-3caa-8da2-4035cdb73185 | -11.28347 | -41.73762 | 2025-11-01 04:40:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 691ba36c-1031-3b88-a023-56f096cd8f13 | -9.86945 | -50.5612 | 2025-11-01 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72b5f943-09cd-3e8d-a37e-6da8a2b3fd34 | -13.67109 | -47.22102 | 2025-11-01 04:40:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cd836165-abb3-3cd1-89bd-a1d338729e9c | -13.38104 | -54.28379 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66652f1a-385e-30e1-b87f-5f32c6319082 | -13.34397 | -48.33586 | 2025-11-01 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6a35b36-4d1e-3d3d-9ed1-414502e6c214 | -9.79021 | -46.96625 | 2025-11-01 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f36fbeb-2d8f-3856-8934-bd56c561015c | -12.52962 | -51.29861 | 2025-11-01 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec4a7111-1ba8-3e05-99d0-8871dc4bb156 | -13.53683 | -47.11027 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05c1dbb9-a661-3739-b440-4e6511cdc0f1 | -11.46744 | -49.80407 | 2025-11-01 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9527b610-129d-337f-bb71-58e6c8845d2f | -13.84903 | -47.06227 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf6668df-b02f-3ef7-84d5-5be0d4335e17 | -11.73428 | -47.46645 | 2025-11-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6646ee86-e028-352d-90ff-5d6e257aa489 | -12.17362 | -53.62662 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 964735f0-9f1e-3c45-bc39-29437ac52fac | -12.17292 | -53.63076 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71cbd928-2bda-3261-a868-a6a0de8738b3 | -10.67903 | -44.09182 | 2025-11-01 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f08d5f5-d185-3760-ab37-5df45d503c61 | -13.00387 | -48.77085 | 2025-11-01 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93a86377-4074-33ad-a2e5-bf20a102bb7b | -13.53311 | -47.1097 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27364d9b-30b2-31a6-bb54-de2ef5493660 | -12.47073 | -48.14162 | 2025-11-01 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54f38bed-62fd-3ece-963b-f3431060ae1b | -11.33854 | -54.3832 | 2025-11-01 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 695ff660-7b27-382b-add5-bdfaac40164f | -13.52507 | -47.11292 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56361b5e-479a-36f2-b1bf-befe80cd9108 | -11.73726 | -47.47116 | 2025-11-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1396394c-671f-3189-85b8-3be9015dfddc | -13.51387 | -47.11152 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d57a3e87-4f3b-32be-b955-98c8677fc756 | -10.63086 | -52.18646 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 56272da3-8d2c-3d5b-8412-ccd2250d8951 | -13.66925 | -47.20741 | 2025-11-01 04:40:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac8a83bd-e37b-312b-8a78-62833ccdd43d | -11.7345 | -59.30533 | 2025-11-01 04:40:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ffd937c-5133-3abf-9dbc-bdf56fc809ee | -13.65227 | -44.4032 | 2025-11-01 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 765a00b0-bf1b-333d-9e78-cf88fb68dcbe | -11.33104 | -54.38195 | 2025-11-01 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff6bc991-8718-3f8b-ab35-92cb2a6b4831 | -11.63963 | -48.56679 | 2025-11-01 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 337e08f2-a20b-39de-b10c-e1514f9dccb5 | -13.29714 | -41.93212 | 2025-11-01 04:40:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59e892e2-caee-33c3-8d04-f18deae1dfc2 | -10.64512 | -52.18495 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad1dff8-39e9-33ef-b4f0-ef1406960986 | -10.63549 | -52.17951 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c68c5d2-bb7b-3ff8-8e61-9bb3362bf6b4 | -11.74647 | -59.29806 | 2025-11-01 04:40:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64d6d432-6150-329e-a328-a962429eae9b | -12.88943 | -48.27059 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c47da5eb-103a-3cc8-a110-cf5379949aae | -15.55725 | -51.49562 | 2025-11-01 04:40:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db8910a8-006e-3007-860d-3c787adc76bd | -10.63766 | -42.3078 | 2025-11-01 04:40:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0872d906-d1cc-315b-927f-e97e01034f60 | -12.02718 | -63.75126 | 2025-11-01 04:40:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9df3e675-6aaa-3a8a-935b-13e15f3e0192 | -10.417 | -44.5023 | 2025-11-01 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8dfa53b-4412-3554-8da3-43019f53a9c7 | -12.59849 | -48.3366 | 2025-11-01 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 235d5524-e75c-3c5c-baf8-1ac4de095850 | -12.02593 | -63.75742 | 2025-11-01 04:40:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bd27c1e-0319-34cf-bf55-4b61ea409000 | -10.63648 | -52.19509 | 2025-11-01 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
