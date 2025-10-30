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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 539f6f7d-beac-310e-981c-aabccb7da025 | -6.14117 | -41.71684 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 27d23fe4-1e8c-3090-b373-55a1538360de | -6.10831 | -41.71485 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7f212ddb-5f45-34ae-b199-e376df761e91 | -11.00223 | -47.87907 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf7b49dd-f23d-3c74-a5c5-bc7373ae9040 | -3.93614 | -50.32694 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d43343f3-88df-3a97-9208-91d60b797785 | -9.94134 | -47.1788 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b7ac69b-290d-3fcd-be39-cac1b8993279 | -10.86311 | -47.62189 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96a6304a-cd6f-3545-8174-0347edc07dfc | -7.26728 | -46.89862 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72ebda23-e599-330f-ab3e-1be2b8a28e77 | -4.55486 | -46.68884 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7a9ffbf-5bfa-3a1d-b37c-6199a5217694 | -8.51725 | -48.94372 | 2025-10-30 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 571de770-512b-355b-b0ee-70bd64790fcc | -10.49316 | -44.1372 | 2025-10-30 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7c54fae-9200-36ae-b630-762b373c4d3d | -4.31572 | -48.22837 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad5bdd86-f9ce-35b8-8982-430931386936 | -7.37354 | -47.61879 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c90da8d-0c20-30e0-ae66-b2050ffde3fa | -9.88932 | -47.44253 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 155f9efb-806b-36b8-9f4b-38f60d29a7a4 | -7.11748 | -45.19566 | 2025-10-30 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 754c6b42-8a4c-3a41-a200-064a22e8392d | -7.90992 | -45.66584 | 2025-10-30 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fb1f212-a5b4-3154-a227-650f4af70ead | -11.17422 | -45.21725 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdf01b6d-d465-34fa-9df1-0e7b36eb6eb1 | -7.32326 | -42.47978 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5ab89dce-c77d-3168-8083-0bf3ab294f45 | -5.43787 | -45.33657 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc1b6371-3d1a-36f2-8a8d-71ed2dc2257b | -7.80329 | -46.45516 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7a099b16-4622-3b08-8016-6c0663634e8f | -4.98761 | -45.93067 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7d839b8-ea7c-3357-98d6-7461beb60d24 | -11.00279 | -47.87555 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e9dcd6e-10a9-3064-be13-1d28f22a0536 | -7.78858 | -46.41698 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ae28210-6172-3ab0-9959-4b354acc26e8 | -7.92863 | -45.5025 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cda3d442-443c-3fbd-83c2-cbb149c71259 | -11.06807 | -47.52972 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bef503aa-0a28-3965-af49-9e408f51f922 | -11.9627 | -43.28622 | 2025-10-30 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 228d1708-8d5f-3719-8bf1-a5e3345729bf | -6.85638 | -46.29739 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5db4f56-8960-311a-9a23-98a29343b4c3 | -9.49918 | -40.37254 | 2025-10-30 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ccbc0c28-d287-3f73-ab31-82dbeaa6da44 | -3.82262 | -52.39231 | 2025-10-30 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14447ec5-f621-3094-8ec2-0583fc651919 | -9.85019 | -47.68809 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a26ae40-fc81-3ad9-bb31-2e3317c8ceec | -10.76458 | -44.73683 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 736bd657-a06d-3da5-a51e-0a3659bd15e1 | -10.27311 | -48.05777 | 2025-10-30 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d41d6a5a-48fc-3932-9931-c95e6882c299 | -7.88033 | -46.74079 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecd72b03-8656-3d05-9e06-ce0d82478844 | -7.78311 | -46.45161 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09bdf283-e704-301b-8b49-3c89e578cd8e | -7.5354 | -47.30776 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ba5aba9-4be3-3cf5-a3ef-397a8bcff07c | -10.74194 | -44.74515 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| faac04fc-3946-390d-9617-89eb8397203c | -10.74133 | -44.74915 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a3bfb3d3-4390-3049-ba37-4b6143988b82 | -11.32781 | -47.96884 | 2025-10-30 04:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c785d71e-45b5-3842-97c2-51e1aba1cc6c | -11.56405 | -44.97629 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1571018b-654b-3d69-9927-6d0fa37fa6cf | -6.14873 | -41.58306 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 10cdb888-a648-3224-bcad-a18ba56d6edb | -9.90607 | -44.90102 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 19e69ca9-9058-3b01-b348-3fadd2773f46 | -9.88199 | -44.8785 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1db3bc8-0113-38f8-a93b-f287db5c9efe | -7.78912 | -46.41352 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 981f174d-17c5-3d43-8ffa-8189aea97637 | -4.23167 | -55.66232 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dbb3175-0a3a-3772-896b-28882c69c9e1 | -9.84474 | -44.89206 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e20ab47-26a8-37f3-bb33-60e50a5bec9a | -7.06623 | -44.9503 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63adba14-0209-3395-ac3f-faed2277edc7 | -8.64995 | -44.80572 | 2025-10-30 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee871643-0aef-3eb9-a3ad-99deaeda9212 | -7.2857 | -46.43999 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5931fd8-a885-3219-a085-134fe1d002db | -6.61769 | -47.17856 | 2025-10-30 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5fffc51-c789-3a8f-bf38-93afffc5e943 | -5.46093 | -40.87652 | 2025-10-30 04:25:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f36e27ca-b152-3b24-ab39-28b389eb5b16 | -10.55465 | -44.84406 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04a1fb2e-223a-3d7f-9557-a1814de1b8d6 | -6.62045 | -47.18261 | 2025-10-30 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af95fa5f-a740-3d02-8270-c840bb01dddb | -11.18223 | -45.2107 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c02af785-ffc9-3862-8995-eaa1b6f81fc0 | -7.50141 | -47.05103 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e89bd7c-9d1c-3457-8058-7988d2e80507 | -10.84529 | -50.12558 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ec81738-46ee-337d-b984-f2d6fc73c869 | -4.84364 | -45.85114 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e58ac09-c642-3cf0-afba-74a2a196b0f6 | -8.0138 | -49.71384 | 2025-10-30 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67cbd397-10a5-324e-8742-8775083876cd | -7.32702 | -42.48037 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8665030a-909c-3320-9edb-4820c9449036 | -9.9474 | -47.18336 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0e4a5bf-7d94-3dc0-9178-ab0e85db1ad0 | -9.89123 | -44.92964 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf7ac909-4d7b-30f7-bdec-eb5b9a637524 | -6.45775 | -46.47481 | 2025-10-30 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b2a7517-3925-37ed-990c-c9fc64a4fd48 | -10.27746 | -44.5692 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00c33d6e-647e-31cf-a82d-9beab5767d64 | -4.5343 | -54.96898 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb597dc9-8eaf-3916-8aae-211da0271edf | -5.52803 | -43.83482 | 2025-10-30 04:25:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e35d418c-4098-3e53-81be-c59d8a415e3a | -5.30195 | -44.31971 | 2025-10-30 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b08b6511-815f-38a1-9ddd-14179db73567 | -6.13982 | -41.68993 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 63b3bd3d-6e28-3d50-9e30-dea8cea69002 | -6.63149 | -44.60716 | 2025-10-30 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2acc1c39-9a7f-39c5-b76d-6552cfd2718d | -6.12547 | -42.44181 | 2025-10-30 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0e9fc1b7-c426-33f0-ab24-3dbde4dbacc8 | -7.78748 | -46.42391 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c0a6292-5d51-32cd-83ea-f797b34f02cb | -10.65017 | -47.76435 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24f697e4-9f28-384a-ad18-04de746e5afc | -6.13741 | -41.6797 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6f6831c2-9ed0-36d3-8c70-1d3ccdcf5931 | -4.89173 | -45.43868 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21841944-6777-34b7-a37d-16bcf965010b | -4.80079 | -46.61704 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c379a61b-16a9-3c74-970d-7cb7f1fe85aa | -6.99971 | -42.29294 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d3b1135-7be7-3a2c-a163-0a02061e33eb | -7.90162 | -45.67533 | 2025-10-30 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99f257be-4bb0-3be5-aef9-6626575e5cdc | -10.9014 | -48.00051 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8acc4f01-08bd-39b7-8802-d26d81c831d4 | -7.31055 | -47.81834 | 2025-10-30 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6494c515-7513-3bf1-a0c5-ab067c202b73 | -7.6208 | -43.58042 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7c69c76b-e491-3508-8c88-d7f6d1fcd35b | -6.133 | -41.70864 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 61428074-46f2-34a1-aafe-fc50b9a4a51f | -7.59527 | -43.60534 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d180d12-03f9-3778-85b8-cd87db7096ef | -3.9717 | -51.07407 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b88c82a8-1865-363d-ab97-f2e1ad07821f | -5.79941 | -40.80902 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 714da776-b2db-3219-8847-8bca8ba6d769 | -6.11131 | -42.43518 | 2025-10-30 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ad4a72a0-4fe2-370a-a1f6-516f95c65203 | -7.26505 | -45.02503 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b959423-a5fc-335f-bd1d-4ee79fd6afb6 | -8.33193 | -47.93052 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58d00a37-eee7-38d3-af45-2e7db8eaf1c9 | -7.96292 | -46.7113 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4c66df4-4b9d-30c9-8421-270f94d31fb2 | -10.90529 | -47.99749 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9193231-8240-3f7e-a119-18f7fafdfd4f | -7.60839 | -43.56611 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4590f4fe-431e-3797-92fa-c003a78292d5 | -9.8341 | -47.70348 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e8b154b-c256-3196-bf0f-fa92eed9ee10 | -5.07555 | -45.17686 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d58bbc73-983a-3a11-ab25-996767e2433d | -10.88461 | -45.07344 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c053e31d-159f-3da3-adec-7e3c0515309f | -6.64859 | -47.28466 | 2025-10-30 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69f7c1fb-229b-3ea3-9a3c-bbd8d30b8a2c | -4.67814 | -45.80395 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c85bea0-45b8-30da-bbf9-ed19d279b242 | -4.91246 | -45.67542 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 579afae4-e85a-3027-915f-fb674091e3f5 | -6.13972 | -41.67254 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fbcca9f8-71be-395a-a702-ec67fa826858 | -6.14077 | -41.69252 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac35e350-70ec-3da6-854a-4454b3ea0c1a | -4.6803 | -46.54038 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00311489-a084-31b3-9b99-dbbe37e5efac | -10.88404 | -45.07726 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e555c47-3acf-3fec-8273-491febcbd402 | -5.61031 | -47.12659 | 2025-10-30 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 04ead4b2-2894-3813-86c4-4adcbeba3421 | -11.54962 | -44.68708 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bce0088-969e-3246-ba89-2061441a38f3 | -10.99233 | -47.85586 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README47.md)
