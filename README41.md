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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 250eb9fd-7365-306c-a8fe-c2efa846fd36 | -8.82432 | -50.05324 | 2025-10-17 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 52e02cf7-8e27-3f7b-b637-2e7c9ad76f05 | -5.68807 | -42.6783 | 2025-10-17 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f990f324-3bcc-37ca-a5cc-a0f6747e4915 | -7.37358 | -44.68838 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c47dd487-d8d5-3bd8-aeca-e7afb2f0bcce | -7.45564 | -42.68158 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ab08c65a-f801-3fe0-83be-c7a47b4176a1 | -10.26283 | -44.03667 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b6c63913-80fd-36f5-9cce-9a16b1af1108 | -9.15982 | -46.60867 | 2025-10-17 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8882800-50f9-3f7d-ace8-bbf2586ab1ff | -8.15727 | -44.00118 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9bb323d-fe14-3f08-9b2e-918c02de42cc | -8.3795 | -46.3179 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 071535e3-6969-3673-ac2b-5cc1e405a6bb | -5.88936 | -43.88763 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 96f02b28-798e-3253-9883-b114c98cf2e1 | -5.31047 | -42.65062 | 2025-10-17 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 849fa4ef-dad4-39be-9733-09273ddbbcad | -9.66722 | -43.8896 | 2025-10-17 04:19:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dca68910-7d75-31e5-b980-8bff96667a55 | -8.33206 | -46.23326 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07c13a6c-31ca-372a-944e-a1eb5bcd300f | -10.08626 | -45.33745 | 2025-10-17 04:19:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 066b2d1b-a8ae-3198-9412-5a600a8c1ab7 | -8.3081 | -43.41812 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 786ac3e8-2007-3ca3-bea5-a6b8b3111a49 | -11.47357 | -44.25881 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ea7f4a3-8d1a-3ee0-8f0d-356f6bde905d | -6.09058 | -42.38749 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 04cf0204-e230-3a53-bf7c-a682805a963e | -11.41219 | -44.20797 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fea352ab-7747-334b-b919-f260089c5fd0 | -5.35018 | -43.39261 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3db92372-8f4c-3e54-81a8-a0eba21143eb | -4.25443 | -48.54905 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75e225e2-4a37-3544-8741-0e09c1ab9a3e | -11.50101 | -44.05556 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3234bfda-322c-3d06-96c2-58b9eb3e8e99 | -5.83806 | -45.53788 | 2025-10-17 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 972dda2d-2b67-3dc5-8c42-bc7098a8b32e | -6.70456 | -44.37748 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6bcbdb3-78a6-36fc-898d-a57ed35eb8dd | -6.15358 | -40.91299 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 30cfb2b6-2482-314f-843c-aa85cc7fe834 | -5.48625 | -43.54678 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8913bd67-0292-3d62-bf58-547d2f3e7d86 | -6.95543 | -41.55901 | 2025-10-17 04:19:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b7e170e3-6a18-335c-9e25-8be9b8fa9fdb | -5.31284 | -42.92936 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2c47452-27e6-3b6c-8094-8e4e22be0bee | -7.90284 | -44.98515 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d866d61-ed0e-3f19-aec4-b1d9a38149c4 | -6.2581 | -44.49072 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42ae1a92-c98a-34ee-ba82-1a6059510502 | -5.79604 | -42.50073 | 2025-10-17 04:19:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bff9fc46-d3b4-3694-ab05-bab1d1434af6 | -10.13651 | -44.57423 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c71624d6-8d31-3048-9a3a-2b997fa6761a | -4.4964 | -49.64395 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a5645ff-29b2-38a8-a8c3-964d7d3fa292 | -6.35685 | -41.4888 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 91b96bd3-d35c-3686-b90d-12a5957d631a | -5.87883 | -44.76212 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab4b6196-9e59-3724-80ac-cec462180cd6 | -11.38409 | -44.2111 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ed36d5c-c551-3611-8202-4efb88968602 | -8.38562 | -46.32253 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e2802d6-565c-3ada-a7a1-0deeb3c0ba23 | -7.45661 | -42.15277 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 086445c0-2eca-3c29-98de-75b71bb1497a | -2.87459 | -50.72443 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e2efc92-5f9c-357d-ac8f-679127617331 | -5.22338 | -46.18882 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a2fac32-d2ed-3193-b661-0f9b7b08b788 | -10.58302 | -47.43227 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4fdb7815-7d78-3780-a6f0-db300056e05a | -6.38382 | -47.69942 | 2025-10-17 04:19:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f3f479d-15ce-3ec6-a651-896e8baa2cd8 | -7.4081 | -44.75396 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfacf998-641c-301f-bad0-c2588fcff07b | -7.95467 | -44.12524 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29819ca6-b346-3522-8d71-b4b3f65b035b | -7.16373 | -49.91758 | 2025-10-17 04:19:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4215ad1c-c89d-3876-8adb-75445936dade | -5.395 | -45.71025 | 2025-10-17 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cead20be-2191-3f86-b3a4-56b6534daead | -10.5289 | -49.55556 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff21169d-17e6-36b4-b2d1-5c371a8d2916 | -5.49274 | -42.16282 | 2025-10-17 04:19:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 22760ee3-f34d-3cea-8252-dc6a4c809d5c | -5.55971 | -42.98553 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 89f660ef-276b-351f-b8b7-b7286fc87038 | -10.48027 | -44.46032 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8d540e9-fc53-39b4-8086-e9e4ebd7efbc | -7.17991 | -42.37449 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6a427a0a-8d8c-3b69-940e-62d43769e2e8 | -5.72409 | -43.83359 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcc1794e-cc0a-3661-a2bb-47dd7b1ec726 | -6.68931 | -44.27604 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 646dcec1-c848-3dc1-8184-198abc1ec3bf | -9.28949 | -46.90863 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f64b97b-e4d2-3432-8bb2-015ece399661 | -7.66907 | -42.568 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8cbeba30-cc28-35d7-967f-4734a8e6a261 | -10.72375 | -47.58155 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72032a18-5c35-3ed8-8af5-89148353c5ef | -6.13511 | -41.7411 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 867e87e4-fb7b-3902-ba97-c14bdea9e007 | -7.94911 | -44.11719 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d2914237-39b1-3edb-87c9-61e5df7e91d6 | -11.41784 | -44.21636 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 091e646e-4d65-3506-bcd2-b7b10d0f1223 | -8.2265 | -43.44345 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c09290e3-85df-304b-a7c7-046a695272b7 | -6.35265 | -41.49237 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d869a94c-fa01-378a-af19-10ec5b8d1d83 | -6.35326 | -41.4882 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e5326d55-478d-3fc5-9ba8-ab2601496588 | -3.52496 | -50.31078 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c43ef389-5a65-3d55-8fdb-e8c219fea47a | -11.45407 | -44.04446 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bb52d41-df61-3d65-be45-860502ceb202 | -9.34282 | -46.90964 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b9f16a3-79f8-32c7-8f7f-750a4ba6986f | -7.95956 | -44.09352 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 560b2f3d-1138-36db-9d5b-396e71686034 | -6.83493 | -41.71193 | 2025-10-17 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d68d4f43-4f13-3374-b13c-865a3e85bb99 | -4.00778 | -44.17027 | 2025-10-17 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5949cf75-b249-39e8-ad59-98448f0f2a34 | -9.24391 | -44.3656 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4b315c9-974d-34d4-bdeb-c7a00a8a2888 | -4.93172 | -41.55399 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 56330781-796d-33fc-801d-95359a7a77a1 | -5.9079 | -44.74902 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0bfee042-d2c8-3a9b-93e9-f3e3262dbe0a | -3.28663 | -52.54442 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a712ed62-e9a4-3a15-b963-c92d64ac13a3 | -11.42515 | -44.21375 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2484f796-8d24-34e6-8b10-e3a3adca74a6 | -5.77712 | -42.46363 | 2025-10-17 04:19:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bc61cb29-2dcc-30a6-a2fd-2107a1f82836 | -6.20774 | -41.76284 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aa49ae33-13a7-35e4-89be-0a895b41c7c0 | -5.49494 | -43.07104 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 443a2216-8d0d-3124-b8af-774c5dee4d46 | -6.95414 | -41.56764 | 2025-10-17 04:19:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5a30158a-2ddc-398b-9472-e232a4bb1f4e | -10.57064 | -47.42263 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf383034-3845-3914-9d72-1b9ede8a3543 | -10.65114 | -45.24949 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e91a4e56-7946-3a1d-bf1a-c9e5b4b2dc00 | -7.60396 | -46.87993 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 526438ba-a132-34eb-83d3-c843b163d7a4 | -11.39783 | -44.11905 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0cea5c11-b4a3-36df-a302-7d712654d161 | -10.49406 | -43.41027 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28530091-d740-3203-a57b-e132d8bad06e | -8.20098 | -43.31587 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 05f03c14-eba8-3291-996c-01899c041cf8 | -5.61355 | -42.68209 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3242f873-0ab0-3347-a65d-2d765430b6b7 | -5.09619 | -45.42744 | 2025-10-17 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f107660-59b9-3c5d-80a8-1d4bfc4cad0e | -2.51729 | -51.93307 | 2025-10-17 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2efdca43-d814-3998-854c-b4cd2cc60047 | -5.9911 | -44.152 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 020e64dd-5fa8-3b1a-ae6f-b63c29ed2b9c | -7.07015 | -44.7392 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8f76fee-c6e8-325f-a1bf-417fcb5d11db | -8.10311 | -44.98475 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d48d9f79-5c54-3d63-a590-b54c6ff48197 | -6.84028 | -42.41561 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8da95c77-73bb-3fe0-b613-c2efc0bae20c | -11.49144 | -44.0958 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ef71a22-d2ef-303c-8a4e-e11ffccbbca9 | -6.69552 | -40.8644 | 2025-10-17 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f914e151-5f9d-39b6-981a-26a360226a9e | -10.2752 | -44.04594 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c90a6397-2356-39f7-b5cf-42a35f3cd7f7 | -7.89571 | -44.98757 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ef3d00-9926-3226-99b3-851d407e279a | -6.10169 | -43.4157 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07447041-d856-3020-aaba-1b5bd9458f78 | -5.86761 | -43.91613 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97678111-b42d-372a-8d65-625aaeb5d8ff | -10.26901 | -44.04134 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe46a85b-1ef9-3de3-a058-f3ccb473ec2e | -7.43771 | -43.74839 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3b684817-5e58-3bfd-97cc-46791560c3b9 | -5.67061 | -44.11213 | 2025-10-17 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 670a934f-485e-3faa-9023-bb7bb6fbf017 | -7.57295 | -43.93202 | 2025-10-17 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bde1d866-a5ea-37d5-acd2-f7ee1102c04d | -7.97061 | -44.08801 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acd7ca1f-ef23-3c6b-b0fc-57a5953e2eaa | -10.29204 | -44.04846 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |


[Clique aqui para ver as próximas entradas](README42.md)
