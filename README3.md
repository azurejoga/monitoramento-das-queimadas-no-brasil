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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db4b0947-66da-3f15-8afa-dbc435a26765 | -7.147 | -44.045898 | 2025-07-30 00:02:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 179edb33-c1d5-3758-864c-5bec4c5a99d5 | -18.570801 | -44.409698 | 2025-07-30 00:02:00 | METOP-B | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 481cfb2d-d61f-3c38-bd0c-61d110e303b4 | -15.7063 | -41.9226 | 2025-07-30 00:02:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ccac284f-3f26-3a11-9e22-835530d246dd | -5.246 | -45.209 | 2025-07-30 00:02:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 892a17c8-9d47-3eb0-855f-62611ed28478 | -7.209 | -43.095901 | 2025-07-30 00:02:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0eb9d515-0535-3ebf-9688-fdf16f927be9 | -9.6359 | -43.842899 | 2025-07-30 00:02:00 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 149016c7-1022-3489-a0e6-a154b607d96a | -10.9653 | -44.491299 | 2025-07-30 00:02:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8db2ea4d-60da-3052-bea1-9da3bd1a1d61 | -13.0975 | -47.291901 | 2025-07-30 00:02:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a4df789-d20f-3823-a5aa-a91ab4ac7d7c | -9.0468 | -45.0755 | 2025-07-30 00:02:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc76e14d-9183-39af-bbd2-5310b0691b05 | -7.3092 | -43.399101 | 2025-07-30 00:02:00 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ac261c2d-a875-315f-921e-45544d736a2e | -3.5021 | -43.243301 | 2025-07-30 00:02:00 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bcb0775-60f8-397d-b7b1-b1631e17a3e1 | -8.9603 | -46.737801 | 2025-07-30 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d731c6da-40cd-3be8-a134-046f1c773f5a | -12.4756 | -47.254101 | 2025-07-30 00:02:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bc2eff6-56ed-3660-8a9a-8cd44a6fbe00 | -12.4872 | -47.260601 | 2025-07-30 00:02:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27f716cf-806e-31e0-a8aa-fe1992045248 | -11.4613 | -45.1077 | 2025-07-30 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95d13890-1b5d-3170-975f-f12cd602e73e | -14.7421 | -46.293098 | 2025-07-30 00:02:00 | METOP-B | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ed4c2583-693a-3e89-9a44-ab808ebad724 | -3.8353 | -48.943401 | 2025-07-30 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fee67ea-73cd-3a49-87a9-0694ebadbe70 | -5.7627 | -43.8946 | 2025-07-30 00:02:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75c49952-2c29-347b-8464-af033ab71b02 | -5.4764 | -42.149601 | 2025-07-30 00:02:00 | METOP-B | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9418bf0e-f09a-3880-a3ca-06421c0481c7 | -7.7818 | -44.988998 | 2025-07-30 00:02:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 668f36f5-2354-3542-b443-dc8772c8dc9a | -7.9381 | -44.0812 | 2025-07-30 00:02:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6670f76e-63f3-3779-862d-1e8f5bcdadd9 | -6.2594 | -46.101601 | 2025-07-30 00:02:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3955987-922c-3ac3-b283-74ea93f56cd9 | -12.489 | -47.2691 | 2025-07-30 00:02:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62c13c3a-8cb6-33f8-a759-f4929c58d894 | -9.1848 | -48.831501 | 2025-07-30 00:02:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2e28d27-f2b9-37ed-95c6-506ec5cb6041 | -9.0197 | -47.9613 | 2025-07-30 00:02:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ac0783d-032b-3c62-bf92-7df6fd7ef41f | -10.7122 | -48.849098 | 2025-07-30 00:02:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 137bb8dd-48fd-3a33-a397-53d380044af2 | -11.329 | -48.9175 | 2025-07-30 00:02:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0d4b0ea-7abe-3a5c-9fac-b2388d9a3053 | -6.3894 | -47.245399 | 2025-07-30 00:02:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e81fa8d7-7f03-388c-81a7-6730d2494f08 | -6.2512 | -46.110802 | 2025-07-30 00:02:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1098bca8-1ee5-3d67-842a-230c6e8c79d1 | -10.6126 | -45.223301 | 2025-07-30 00:02:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 489323e1-6c3b-3641-b006-0b5fda1ae172 | -4.3753 | -49.016102 | 2025-07-30 00:02:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3541da3-2687-3509-88b3-1bf454088b34 | -17.0495 | -43.766201 | 2025-07-30 00:02:00 | METOP-B | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a96af35f-ce76-39b0-b73c-13015934905d | -10.9282 | -44.185799 | 2025-07-30 00:02:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56bfa354-0028-314e-b84a-9ca4d1b1d16c | -11.8103 | -44.2635 | 2025-07-30 00:02:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c5ef69f4-f565-3227-ad34-63381bb7f09a | -7.339 | -43.7565 | 2025-07-30 00:02:00 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cca01f8a-7825-33a3-a361-6e76831cbe6c | -11.4598 | -45.100601 | 2025-07-30 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07e298b5-f441-3b01-b445-4a429ca9cfbb | -5.1871 | -44.947498 | 2025-07-30 00:02:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbbda6fa-c9b2-3e00-b0cc-cf05f5ab0aeb | -9.8273 | -41.481602 | 2025-07-30 00:02:00 | METOP-B | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 67e13e30-98ed-3503-8d8e-981858bb4d57 | -8.6372 | -45.501701 | 2025-07-30 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 81243b01-5a09-3bac-8225-40b427ff62f4 | -13.5415 | -44.1348 | 2025-07-30 00:02:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 691b057a-bd61-3580-b374-32c211ecb339 | -10.5157 | -44.877602 | 2025-07-30 00:02:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9e08a4c5-70db-3d2d-8f05-0b0779d6bcff | -4.8984 | -44.946602 | 2025-07-30 00:02:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d6bb37e-57ec-3532-8362-cef3959a6462 | -7.1433 | -44.348598 | 2025-07-30 00:02:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4fbf35a8-2f28-3853-a2d2-7f5331ef4c7b | -14.9187 | -45.134899 | 2025-07-30 00:02:00 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 55df85e6-e83d-3d6e-8938-c6f576a7e8bc | -11.5175 | -46.841301 | 2025-07-30 00:02:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1042e7db-88c0-309b-a596-fc624f468f6b | -8.2375 | -44.908798 | 2025-07-30 00:02:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dcdefca1-ea75-348b-9486-2822e7877105 | -13.0895 | -47.3027 | 2025-07-30 00:02:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3a89e7b-31b4-322c-9ac6-15d876acce4d | -15.7211 | -41.9422 | 2025-07-30 00:02:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d48dfca-c1b6-379d-8b23-122bdfcf4332 | -11.4727 | -45.112598 | 2025-07-30 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb0db583-2165-3e59-91ba-c3a8c31a1e19 | -12.8164 | -45.431999 | 2025-07-30 00:02:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3611ed9b-7775-31b9-8c50-1a29a33c4f5e | -7.0975 | -44.3736 | 2025-07-30 00:02:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 296d3c9f-8349-3312-a2da-56993dcbc52e | -10.6172 | -45.244499 | 2025-07-30 00:02:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f9cc43d3-024c-329e-bf49-bb22b59a935c | -12.5825 | -49.767601 | 2025-07-30 00:02:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f7651ae-b1a5-3e32-b318-de49ed4ab361 | -6.5097 | -56.147999 | 2025-07-30 00:02:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05820d1d-3427-33d3-9098-b167afc33b5c | -9.4284 | -40.352798 | 2025-07-30 00:02:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8a9dda1a-ae76-3c48-8344-8faca4dff059 | -12.8151 | -43.089699 | 2025-07-30 00:02:00 | METOP-B | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 86bd6e21-4588-3985-99d5-021d6a90b4f3 | -11.817 | -44.247299 | 2025-07-30 00:02:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c50deb2-3284-32a0-bf0b-b0fa75a846a6 | -10.5277 | -42.549702 | 2025-07-30 00:02:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7a4ef3ff-a737-3b3a-878f-1a1dd4b95037 | -9.4164 | -40.3456 | 2025-07-30 00:02:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7fb7e496-63ec-35a5-9bd0-e72ba8556885 | -9.1523 | -49.841301 | 2025-07-30 00:02:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db9cab24-70b4-3bf2-80e0-115ed084eb88 | -6.4598 | -44.560799 | 2025-07-30 00:02:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7c2c83b-23c8-3422-9f56-ac6f886c6f10 | -8.0206 | -47.657398 | 2025-07-30 00:02:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2264bf8f-1b1c-304f-97bd-9ab0e287d5c8 | -15.7113 | -41.944599 | 2025-07-30 00:02:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36cf3a2f-4879-3853-8dfd-eff9e2b2c086 | -8.0223 | -47.665401 | 2025-07-30 00:02:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99de6800-63dc-3b24-aab1-0a0124835509 | -5.761 | -43.887402 | 2025-07-30 00:02:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| adddb2e8-cecd-31f3-8518-2a7beb5480bc | -7.2252 | -43.076401 | 2025-07-30 00:02:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 848347f2-ce52-3701-b411-d57853fa74f9 | -11.98 | -46.943298 | 2025-07-30 00:02:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81c79c9d-1d45-3459-9848-3f2058d7d1c3 | -9.1621 | -49.839199 | 2025-07-30 00:02:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27ea47b3-5eab-37b1-ac06-8c504c70dfd3 | -19.932899 | -49.886799 | 2025-07-30 00:02:00 | METOP-B | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f835e205-6239-3ce8-b343-5e2302fa1caf | -9.052 | -45.052502 | 2025-07-30 00:02:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6263b483-6f2b-31ea-82d7-fa7d587e61a5 | -10.0951 | -46.952702 | 2025-07-30 00:02:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bceb8224-cf8b-37bf-b219-9d49c7ba800e | -17.4862 | -46.720402 | 2025-07-30 00:02:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9a57eeb-d70e-3ab0-b90f-7509b3864e4f | -8.6274 | -45.503899 | 2025-07-30 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eb93d7c6-2f74-3678-a91c-db500aafb1fd | -12.4705 | -44.084099 | 2025-07-30 00:02:00 | METOP-B | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a35c13d-d666-3ad8-a6f1-b763589a3ade | -8.6243 | -45.490002 | 2025-07-30 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c3c100de-bdca-3c80-bf21-51635b7de7e2 | -13.0877 | -47.293999 | 2025-07-30 00:02:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f08b572-140f-38f1-8a57-26ecb38f066b | -10.627 | -45.242298 | 2025-07-30 00:02:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 76596ac1-0be4-3b28-adf8-1595dd8aaf05 | -2.9857 | -48.588799 | 2025-07-30 00:02:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cff131af-638a-324a-8ff9-d26a328d63bd | -7.279 | -47.976501 | 2025-07-30 00:02:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0350757e-2a4c-38c2-8bd0-9a6627d41329 | -15.7174 | -41.9272 | 2025-07-30 00:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 637.0 |
| 22501f2d-5930-3d99-bc33-af48bb96679c | -9.1538 | -49.857 | 2025-07-30 00:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 72f108ca-806c-3db6-b96e-094f417a79d3 | -4.6511 | -43.1104 | 2025-07-30 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| f09efdaa-cfd2-3a78-9af5-4ca95d494779 | -11.4584 | -45.1126 | 2025-07-30 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| e8766964-5b89-3f53-b5d0-4aaee284645b | -11.4776 | -45.1099 | 2025-07-30 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 54fea9ff-d9b6-3783-932e-f7c3395455e7 | -15.6975 | -41.9317 | 2025-07-30 00:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.9 |
| 4a3186ed-18ee-3e21-aa18-0a2181e35bc9 | -10.6172 | -45.2282 | 2025-07-30 00:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 3734ace8-ecf1-376f-94e4-1267ccabf983 | -15.7167 | -41.9521 | 2025-07-30 00:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 335.4 |
| 5b2fb960-091c-3cd9-855f-359963300935 | -7.8568 | -46.7304 | 2025-07-30 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 1e2e74bb-18b9-3d9b-a6b0-5c7b365b6962 | -10.6169 | -45.2512 | 2025-07-30 00:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 49fe84ba-51ba-33c5-af26-552fad2916e2 | -15.7372 | -41.9227 | 2025-07-30 00:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| da4285d8-8625-3e84-89ab-3bdee507feb3 | -15.718 | -41.9023 | 2025-07-30 00:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.2 |
| d248b0e5-da4e-3bdf-ba80-477c3e2091a3 | -9.154 | -49.8356 | 2025-07-30 00:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| dba04383-3493-30c7-80c3-55247c7f7c11 | -15.6969 | -41.9566 | 2025-07-30 00:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.6 |
| 4319e8c4-4578-319b-b26e-e95f21698437 | -6.5258 | -56.2121 | 2025-07-30 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 9951014c-466a-3fee-90dc-fb8e12ec0a0d | -18.38 | -49.5864 | 2025-07-30 00:10:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 51.5 |
| 7cd49079-5154-3962-b0d8-edc2962932d4 | -2.9108 | -48.254 | 2025-07-30 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 767a5285-6b4a-3cbe-8788-f0c5da645a24 | -8.5211 | -43.3063 | 2025-07-30 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| bca9111d-9da8-329c-9058-2a7c9e683051 | -4.6698 | -43.1092 | 2025-07-30 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 5cc52b22-3f00-3a63-b530-9b446877dcbb | -6.6143 | -59.9848 | 2025-07-30 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 7cf4d740-3a14-3d44-8031-6fad3202c3d6 | -10.6169 | -45.2512 | 2025-07-30 00:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |


[Clique aqui para ver as próximas entradas](README4.md)
