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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a2cb8c3-ca48-3076-86bc-667325b3f18e | -5.2146 | -44.310299 | 2026-09-05 00:31:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74318061-9468-3f97-bf22-0ea4c6772fc4 | -3.4472 | -43.280102 | 2026-09-05 00:31:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17f1a8c7-05b2-30a9-b94b-8c115176d91e | -20.336399 | -47.596901 | 2026-09-05 00:31:00 | METOP-C | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6b52d373-743b-3c25-b984-e7b286b2ec5b | -12.9314 | -42.4305 | 2026-09-05 00:31:00 | METOP-C | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a7d3f4ab-4c5a-363e-82c8-8e491c1d3d84 | -19.8041 | -49.588799 | 2026-09-05 00:31:00 | METOP-C | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9037808-93cc-3447-af8c-2ae077baf4c0 | -7.1342 | -42.253502 | 2026-09-05 00:31:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e1c1a8fc-f0b5-32bb-aa83-e9734f01ad6c | -13.5707 | -44.108101 | 2026-09-05 00:31:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e853c7c-2227-3300-ac4a-8402dd4bccc5 | -5.3212 | -45.167099 | 2026-09-05 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27f91255-fcfc-33c0-9256-e34e494769a9 | -13.5592 | -44.103199 | 2026-09-05 00:31:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75f5727e-ea30-3609-ad17-65b87242eaf2 | -13.5609 | -44.110401 | 2026-09-05 00:31:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d763f44c-b9d5-34a1-b582-e40af997134d | -17.096901 | -56.811699 | 2026-09-05 00:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9cddea1b-b53c-3281-92f9-c3f35a6f444a | -6.3682 | -43.5956 | 2026-09-05 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7636a18-3520-374f-acc2-2aadb3252f66 | -10.4685 | -46.019798 | 2026-09-05 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6215f7ba-22cf-3680-8455-ef9b262007ec | -20.827 | -46.321201 | 2026-09-05 00:31:00 | METOP-C | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac2739d1-8a90-3915-bb7c-a3c57bc24d84 | -3.445 | -43.270802 | 2026-09-05 00:31:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4acb175e-7bf3-3268-96c8-9193fd12c27d | -7.6731 | -46.060001 | 2026-09-05 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0aa37fc-bd45-3e1f-b4c4-6aee833b8ef1 | -5.8464 | -52.053699 | 2026-09-05 00:31:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86262731-2d5f-3e84-af02-5e6285141553 | -19.747601 | -46.696301 | 2026-09-05 00:31:00 | METOP-C | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 91aa6835-12a5-30c5-9655-8865ecc7c97a | -10.4602 | -46.0289 | 2026-09-05 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9bf55f0-fb11-3474-ab84-ca509398815f | -20.738701 | -47.155102 | 2026-09-05 00:31:00 | METOP-C | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 82612380-28e8-3673-b367-b43f9c091910 | -20.174101 | -47.394798 | 2026-09-05 00:31:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 117e37fc-d51c-396e-87cb-a5cec0480567 | -5.9241 | -47.8866 | 2026-09-05 00:31:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c03ab19-4762-3320-8562-c30fea8b6b56 | 2.3859 | -50.767101 | 2026-09-05 00:31:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6f869ade-60f6-3404-96f6-c1ad780702f3 | -12.9198 | -42.4249 | 2026-09-05 00:31:00 | METOP-C | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f8b063b8-f473-3d54-af82-159fc6d8982f | -2.774 | -47.770802 | 2026-09-05 00:31:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f5ae823-a430-3967-a040-bed420e647d5 | -4.3615 | -47.768799 | 2026-09-05 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7953381e-6056-3276-99dd-4c571a918a47 | -5.9272 | -47.9006 | 2026-09-05 00:31:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cff32bb-1232-3aa1-8a0d-73eab7454b9e | -7.6779 | -46.0807 | 2026-09-05 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ede6003-6723-34ed-9b92-8ebef3895861 | -17.087299 | -56.813301 | 2026-09-05 00:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7a11f7c-4880-335e-9fe3-39fb8d0e26f8 | -13.3176 | -44.039902 | 2026-09-05 00:31:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b21f5b15-0aa0-3bf9-b098-87fa104a66f2 | -20.988001 | -45.805801 | 2026-09-05 00:31:00 | METOP-C | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bc759fb6-c175-3a2c-b5e0-bcdbd1a2b041 | -5.2165 | -44.3181 | 2026-09-05 00:31:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6708bbb-c199-301d-a702-2d19483d8909 | -13.3193 | -44.0471 | 2026-09-05 00:31:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1505002e-7ba9-35ef-bcf9-aae2cb88b2e7 | -7.457 | -46.152401 | 2026-09-05 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7c1eea2-daee-39a2-880b-f2957923ab1c | -13.5576 | -44.0961 | 2026-09-05 00:31:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d3ec112-07cd-333f-bc70-0eecba904f88 | -17.2971 | -43.3433 | 2026-09-05 00:31:00 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f33c1048-a895-303a-9122-be962a49a9f8 | -13.4345 | -43.8302 | 2026-09-05 00:31:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c7a26dd-ed50-391d-9d3b-9d1e74010c55 | -19.808701 | -49.6134 | 2026-09-05 00:31:00 | METOP-C | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c8db047-7654-3761-815a-0b2699a15251 | -14.7389 | -47.144199 | 2026-09-05 00:31:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e48ac61e-6db0-359e-85eb-6ff44368abfa | -12.851 | -44.390099 | 2026-09-05 00:31:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eff6e08c-81f3-3cf4-b512-0ce8e4a24b79 | -17.2987 | -43.350601 | 2026-09-05 00:31:00 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 569748af-caab-34f7-8398-8cd88878ebad | -20.338301 | -47.606499 | 2026-09-05 00:31:00 | METOP-C | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ae1cf83a-f9b4-3b78-99da-725a173e9c30 | -19.820801 | -49.623798 | 2026-09-05 00:31:00 | METOP-C | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a489f25-374f-3982-b8d7-a905e0c7fe4c | -16.235201 | -40.291199 | 2026-09-05 00:31:00 | METOP-C | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3769ef52-eddc-3eef-914c-34756899f855 | -1.208 | -47.598301 | 2026-09-05 00:31:00 | METOP-C | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92393860-4000-37b0-8ca1-3c0a20f00f75 | -17.2237 | -53.866199 | 2026-09-05 00:31:00 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58cdd5d0-8127-3098-acc5-876d92f9d38f | -3.4334 | -52.8172 | 2026-09-05 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e3b37f-d3e1-37dc-8360-2d6cbf78488f | -12.8526 | -44.397099 | 2026-09-05 00:31:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1597a7d4-9021-30f8-b216-81ed3c600b86 | -13.4409 | -43.8134 | 2026-09-05 00:31:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 220f45b9-ba22-3d45-99c5-2956d3a4a8ac | -4.3631 | -47.7757 | 2026-09-05 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 628b473e-7d69-32fe-89b4-3c1e48eae535 | -6.2716 | -43.272999 | 2026-09-05 00:31:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 693dae3e-749b-3bdc-8c2a-30b56ebe8d65 | -10.6282 | -42.960701 | 2026-09-05 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 799a7e4f-88f4-3784-9f98-a010ffc0a265 | -10.9354 | -45.351601 | 2026-09-05 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 387e64e2-2d2e-32a3-8501-208af5cf95cf | -2.1243 | -49.529999 | 2026-09-05 00:31:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0aa961e-a272-36ea-93c5-42e9bd098a74 | -2.4515 | -47.578201 | 2026-09-05 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d3dd9bd-8992-37f0-b537-62227a7ed744 | 2.3744 | -50.7724 | 2026-09-05 00:31:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f7b457ba-999e-305b-a9f7-13c0a7debb95 | -19.260799 | -46.8671 | 2026-09-05 00:31:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fdacbeba-318a-39ee-8168-49a728f3a736 | -14.7406 | -47.152 | 2026-09-05 00:31:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1af750b-eea6-36f4-a443-4d12bf7d5c4d | -10.4716 | -46.0336 | 2026-09-05 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92ef9b61-bdb7-3480-b5da-d8329530d803 | 0.1773 | -51.449001 | 2026-09-05 00:31:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 53d555c2-bb05-32a8-b0ed-2f6f472a7ff7 | -2.8151 | -48.672798 | 2026-09-05 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 006a6398-5642-364a-b91c-7166c3feaa10 | -6.3545 | -46.112499 | 2026-09-05 00:31:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bcb6e13-e254-3ba7-88e8-5f30366cfe17 | -5.7639 | -45.073898 | 2026-09-05 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a6f8c9e-3bac-3259-851b-3eae6f67fe60 | -3.4428 | -43.2616 | 2026-09-05 00:31:00 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d83d4875-13ed-3076-b04d-f487558f8370 | -5.6177 | -45.244499 | 2026-09-05 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e38b660f-4273-3a0c-8eb7-4f2e130bdd24 | -6.6697 | -59.9635 | 2026-09-05 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 03df65c9-cd8f-3415-8b31-ab729e62f75f | -13.4259 | -43.8401 | 2026-09-05 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0551c735-7ff8-3b04-9bff-12a3381a710c | -13.4453 | -43.8366 | 2026-09-05 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| bf050e4f-0d44-3595-98c8-7c8c6674e899 | -6.0244 | -60.1781 | 2026-09-05 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c9b082e3-f653-3fa6-8924-d7594e39ff8a | -6.6514 | -59.945 | 2026-09-05 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 180.1 |
| 778d96ab-fddd-3f3e-982b-83660a926fc5 | -10.4713 | -46.0443 | 2026-09-05 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 716de508-0d38-3a85-a878-1903807b683e | -10.2198 | -36.2621 | 2026-09-05 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| 1136e1f8-18b5-37d0-b198-387c247c6814 | -5.3277 | -56.0263 | 2026-09-05 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d3d284c6-ef90-35d9-a2f3-dfeca1d36d43 | -17.1078 | -56.8304 | 2026-09-05 00:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 92c469ef-1ee4-370e-8ddf-e38f4dd1467e | -10.2391 | -36.2586 | 2026-09-05 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 121.6 |
| bc58e794-57e9-3c41-b362-150e725ceac9 | -6.6698 | -59.9443 | 2026-09-05 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 40d2f5b2-97c0-3003-8f7c-4f09253dbbfb | -10.8049 | -60.7644 | 2026-09-05 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1eef7ad1-9b36-3732-b5bc-d463a39b005d | -5.6565 | -60.2475 | 2026-09-05 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 1a6bb4d9-992e-39de-8059-a9e577931b96 | -12.8543 | -44.386 | 2026-09-05 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9f63218e-3be7-3c80-8eb7-9bf3eb60d942 | -3.7645 | -61.7548 | 2026-09-05 00:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 011fa113-d9a6-3967-9450-bf2dcde96d53 | -6.5963 | -59.9087 | 2026-09-05 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| f6c7f0da-75d1-3f19-b0b5-20a07e2ad649 | -13.4264 | -43.8163 | 2026-09-05 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| e2ba9a38-3850-3fa3-be0f-2e39dc360e65 | -5.346 | -56.0454 | 2026-09-05 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| f8cb218d-1678-31c3-9628-0334ab53e437 | -10.2203 | -36.235 | 2026-09-05 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 30290793-8d74-3e0a-86ff-1e7cc718dd90 | -3.7828 | -61.7545 | 2026-09-05 00:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 32ccacb1-1475-35b9-bca9-d6a04dff83e5 | -4.6853 | -55.6343 | 2026-09-05 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| ebf8e4bb-6aa9-36de-af1c-46b6cdcbf382 | -5.9197 | -47.8927 | 2026-09-05 00:40:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| e27e4828-a892-3e78-b577-23f0c73a3682 | -10.4717 | -46.0216 | 2026-09-05 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| cf67a15b-bce5-3387-afb0-bbdc9c14473c | -5.6566 | -60.2284 | 2026-09-05 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 754e3f0c-d461-3440-9a30-31a5fef43c7a | -6.6513 | -59.9642 | 2026-09-05 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.4 |
| a7049d68-abb0-3438-a553-59879e0b18c5 | -8.7514 | -69.2243 | 2026-09-05 00:40:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 49.8 |
| a60dd276-4974-3f3b-935c-c6e8ff8f471d | -5.7571 | -45.0613 | 2026-09-05 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 03c299b8-5c45-3c07-9b4f-362ab728c299 | -10.4527 | -46.024 | 2026-09-05 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| a33d0cb5-bda0-39e8-9b8b-10d264ef861b | -5.3462 | -56.0256 | 2026-09-05 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 79558cfa-c586-39fc-ae3b-8dd511c88e01 | -13.4458 | -43.8128 | 2026-09-05 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 196.2 |
| cac5d405-0884-374c-8901-7ae066f8bdbc | -5.7758 | -45.0599 | 2026-09-05 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 414e9b1e-b8ae-380f-96be-2299f195a4de | -3.7645 | -61.7737 | 2026-09-05 00:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 2ded6738-4d79-3a23-9d12-000a025fc62f | -3.7827 | -61.7733 | 2026-09-05 00:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 39816d7d-963a-36ef-a62a-afaec0d5eb90 | -4.6669 | -55.635 | 2026-09-05 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 74a97948-9845-3b15-b204-9695786b8dc9 | -12.933 | -42.4192 | 2026-09-05 00:40:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 69.9 |


[Clique aqui para ver as próximas entradas](README6.md)
