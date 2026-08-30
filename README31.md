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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99f99667-8e55-3a97-bbe2-231dda72aaeb | -10.35656 | -49.98189 | 2026-08-30 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17b15a08-ab48-3780-8ba9-c16e081f5ef8 | -7.60871 | -45.8394 | 2026-08-30 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 087fce59-d0d0-3bf7-87b4-c2ae9bb52b28 | -9.21317 | -46.06974 | 2026-08-30 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b2d0917-3e7a-3486-8306-92d4fade5078 | -7.11037 | -42.19155 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69759a12-cf77-38ab-84c4-d38251ef3f00 | -11.24857 | -45.32402 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a7e6145-5bb0-3557-9924-485b361558a8 | -10.81899 | -45.32658 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 160069e7-c7dd-36bb-a8a4-49d8999664fc | -7.31682 | -45.34161 | 2026-08-30 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5b5be5c-848c-3983-9f37-80b29facb92d | -7.13234 | -43.16283 | 2026-08-30 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 22d136a4-38b9-3672-90db-d31118ddfd23 | -10.94739 | -43.02606 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| b57f6a16-5c29-334d-82ff-b2f5a7868ddc | -12.65708 | -47.08855 | 2026-08-30 04:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10aa698e-e61f-36b4-8337-5fc6c490695e | -9.21664 | -46.07416 | 2026-08-30 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 21ca36f8-a931-372d-90b7-f94aa293c8b4 | -8.13407 | -45.47739 | 2026-08-30 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f701c81f-d962-3a6e-b5c4-c0fd8173b27e | -11.21228 | -45.05927 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73acb1bb-9498-3592-91f4-71b07d563568 | -8.01771 | -48.00837 | 2026-08-30 04:14:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6116f60b-949b-3064-a7ca-c11a320f30d5 | -10.95239 | -43.03857 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2d66a0b0-c272-325c-bcdc-1e4cda146aee | -11.35411 | -45.15609 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2722b906-97b7-3296-a5f3-c115eb111011 | -10.9502 | -43.03042 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 198431fd-58ae-372c-b761-a5ca5fda40a8 | -11.15995 | -51.30238 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dea06c39-e956-3949-b4f0-64fa1062fb9c | -11.80803 | -51.04829 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| be1e9e8e-d1d2-3b35-8648-44354b90de9f | -11.53389 | -45.55434 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c19b3010-c1c5-317c-bf8c-72b68e68b181 | -11.16592 | -51.31479 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85f08ee0-6c71-37b6-8f29-c2b1427ccf89 | -11.23854 | -54.00724 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf07fabb-14a4-3ac7-8205-ddbd5e9b24a7 | -11.18639 | -55.10656 | 2026-08-30 04:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| db4fbc18-c2a4-35f2-bce8-d4a794240f75 | -12.08746 | -47.19692 | 2026-08-30 04:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e126effe-9654-3e21-8eb4-bad2a1e18d2d | -12.90632 | -45.87772 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1bcd4e6-973d-3f00-b4f3-5ad30dc4aa39 | -12.7884 | -44.61425 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25d33ce8-c682-3e8f-9265-25094a5b4ae0 | -7.94307 | -44.26422 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 64836475-b8ae-372b-b8ed-11c49bbdd74b | -11.22064 | -45.07794 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9151231-e1d0-34c4-a82f-35ff81e7cd73 | -11.34364 | -45.14912 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1fa9089-34ef-331f-bee8-eda3aa408be7 | -7.23467 | -43.11128 | 2026-08-30 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f5627296-e458-3381-a124-a0a024f1c1aa | -15.10382 | -48.16369 | 2026-08-30 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b95584ea-1531-3518-af82-0500d9c56a4e | -16.34289 | -50.97783 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4cf63ba-bcc4-36ad-a790-b6f396e9ce2d | -19.87201 | -46.39971 | 2026-08-30 04:17:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04cd52cd-a4dc-38a5-a21f-903db68c2620 | -19.09792 | -46.24325 | 2026-08-30 04:17:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de5e51c8-a3f8-3491-aee4-88182d8b2ae3 | -14.41277 | -52.55589 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c54cca9-1945-3c81-9888-188201e132a3 | -16.20388 | -47.75902 | 2026-08-30 04:17:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9040f512-58a6-389a-9002-4d889906ad34 | -14.77678 | -48.733 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 800dd270-4bab-3969-aa90-444746d40a55 | -14.24997 | -54.65051 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d46435bf-4c5d-3a58-8d93-c9048972d5de | -14.39949 | -52.56208 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee5f4ba9-5253-3bfd-a960-5378493b1dbd | -17.28199 | -46.0107 | 2026-08-30 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e944efaf-58e1-3a2a-8503-f3cbeae43712 | -19.09511 | -46.23806 | 2026-08-30 04:17:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df1ea3e6-79d5-3ea4-a712-312980d03f2e | -17.79165 | -39.70769 | 2026-08-30 04:17:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f6981eeb-e083-3766-b868-a2dff872f954 | -25.62255 | -50.67023 | 2026-08-30 04:17:00 | NPP-375D | REBOUÇAS | PARANÁ | Brasil | 4121505 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| efa1ae12-7e6a-3dc8-8f39-9ed1fe63aedd | -16.34738 | -50.98154 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a8c152d-0406-3c23-86f8-8bc09ab3b13c | -14.39869 | -52.56594 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f045028f-50e8-3712-9708-73c33a8e6b10 | -19.08546 | -57.40081 | 2026-08-30 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 28256e65-000c-3412-8004-da20e8c12b78 | -13.85427 | -54.10795 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b352834-3f4d-3940-8b13-9f65ae7d6689 | -16.3584 | -51.00502 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7109347d-bf50-370c-9f8c-c7ec1c14a7c6 | -14.40033 | -52.55798 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d128672-30a1-3795-af10-df904a831990 | -24.28692 | -49.6006 | 2026-08-30 04:17:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 553efdfd-9ca3-341f-8503-c5903e529e3a | -14.20584 | -52.85745 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c32fa3b-ea5c-3f7b-8819-53baa9d7b36e | -14.4413 | -52.56106 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7db492b9-12f7-3341-b279-1531bf7e1891 | -14.67553 | -48.05352 | 2026-08-30 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f70875f-2114-37e9-a119-c001614eda6c | -19.87155 | -46.39682 | 2026-08-30 04:17:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb9dcebe-011f-3f28-b180-ac5061f3fa6a | -14.43554 | -52.56197 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14c3f6f2-8028-323f-9e6a-2fc6c1407d75 | -14.4136 | -52.55185 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a2b0e04-aabe-34a8-88d3-db255991441f | -14.20493 | -52.86184 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b63af0a4-1afa-38d1-a7b1-a8038775f434 | -14.41844 | -52.55754 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0020b6ac-fa3e-3e19-af74-79635ae9e17d | -16.11131 | -47.92718 | 2026-08-30 04:17:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 306b7594-504e-38a5-8289-2ae9b810025a | -16.34682 | -50.98435 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0316c5aa-d309-39d5-bbc7-e6bddfb85279 | -14.93438 | -56.33744 | 2026-08-30 04:17:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68ebb698-e47e-3ff0-ad3f-9bc408e8e5f0 | -14.24233 | -54.65431 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c6185e1-dbac-37d5-a3c1-207170556094 | -14.41926 | -52.55349 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b34abd9-fdf0-3873-af30-a46e4ac22d91 | -18.82071 | -47.45897 | 2026-08-30 04:17:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 255e54b3-942f-317c-9642-b0db8d6b02ec | -14.76709 | -48.73524 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71767ace-d737-326c-a7a1-eb60f0799283 | -14.19254 | -52.86228 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06c25bc6-c55b-3488-9d53-6a67a59c8568 | -16.33969 | -43.43984 | 2026-08-30 04:17:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8227b58f-76fa-3de2-9592-92618ef7e555 | -16.33908 | -43.44353 | 2026-08-30 04:17:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2574b93b-30da-3b92-ba66-334f912f0b40 | -19.09236 | -57.40274 | 2026-08-30 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 51496499-3ac1-3106-92e5-cdce4cd55080 | -14.94145 | -56.33911 | 2026-08-30 04:17:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db11ea7a-b1c7-3a24-a429-b2717d9c3837 | -17.42369 | -42.63194 | 2026-08-30 04:17:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05d6e8f7-bcdf-38f5-8d45-9a1c8318d474 | -14.02925 | -54.01648 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3087f503-7499-36e5-894a-09f23706dd1f | -17.86286 | -44.29563 | 2026-08-30 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12ef864d-ce60-33ff-bdac-b531772fce6c | -14.19745 | -52.86818 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ee127a2-6919-3fec-8356-13e2f6c5f4ce | -18.89765 | -45.81111 | 2026-08-30 04:17:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c24ea4ee-c883-37a7-8cea-f2f41fa7768f | -24.28795 | -49.60211 | 2026-08-30 04:17:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caaedc42-acea-322a-abc1-d0117a8039bf | -16.28014 | -42.57203 | 2026-08-30 04:17:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bbb3d08e-4314-30c2-b43f-60f1ef33ae26 | -13.87003 | -54.12803 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 84b3f32d-dfc7-364f-bb0b-656bb8c137a3 | -20.20621 | -40.39557 | 2026-08-30 04:17:00 | NPP-375D | SANTA LEOPOLDINA | ESPÍRITO SANTO | Brasil | 3204500 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6e8ef5d2-162a-3bab-baae-c3a29d411277 | -18.66141 | -46.84573 | 2026-08-30 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9641119d-8f68-318f-8abd-23fa034822e7 | -16.54707 | -49.39017 | 2026-08-30 04:17:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6660f628-ccd8-36f4-8e98-a222dec20498 | -19.0903 | -57.40191 | 2026-08-30 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 32cd544b-3cd1-395d-aec7-657ee008af77 | -21.19369 | -46.82149 | 2026-08-30 04:17:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7be83024-d665-3dae-886a-1ed22b75438b | -21.19447 | -46.8171 | 2026-08-30 04:17:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2556ff65-7d32-32c7-8aca-600ebd109431 | -21.60724 | -46.06691 | 2026-08-30 04:17:00 | NPP-375D | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 09dad021-26b4-3330-91dd-96f0a86528ed | -13.3981 | -51.76343 | 2026-08-30 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c2b3644d-7c68-3497-b873-d36fef8f69ea | -16.8946 | -39.31161 | 2026-08-30 04:17:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 750419ce-9d7e-349f-b020-50d331de8be9 | -14.1559 | -52.81658 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bd504c7-8887-3b01-a914-7dd08f2ff15a | -14.20403 | -52.86615 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec3efcda-53b1-3019-91ab-24a4e8e0482f | -14.33985 | -47.23058 | 2026-08-30 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfd9574b-1f19-327c-8ab3-8a716c470e8e | -14.19832 | -52.86406 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 339edd67-3e1d-3321-9c0d-9f8f28f80ea7 | -15.10883 | -48.16068 | 2026-08-30 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 944a51d9-5ebb-368c-818a-e672919a226f | -16.35134 | -50.98792 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c9e64a1-4b67-3d34-ae33-833ea0e243e7 | -18.87892 | -46.38238 | 2026-08-30 04:17:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65be881e-e065-31df-8796-de3a03d50ad2 | -18.52892 | -42.1567 | 2026-08-30 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0d17ce69-d9f0-3370-b002-9a00089cf967 | -14.24712 | -54.65247 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3e6a290-0915-3f37-b5fa-65ba1f1c2cf9 | -17.8635 | -44.29183 | 2026-08-30 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e30b956-85d6-3c8d-8150-0b78f9efa8b1 | -16.71837 | -47.63811 | 2026-08-30 04:17:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36ecee71-9be2-3782-982f-fd588354c304 | -18.52672 | -42.14877 | 2026-08-30 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d1c5cc89-8a5a-3cf1-bd2e-b1f0a7a3a60d | -15.653 | -45.91234 | 2026-08-30 04:17:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
