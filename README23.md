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
| 3a9b7f42-3ff7-34fa-8860-569a59d20528 | -3.32963 | -50.50238 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 371ab6be-a13b-3bf2-9b0d-be45d92dd272 | -4.27663 | -50.89137 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b207a3a-66fa-35d3-a964-79d35a09f12d | -6.53631 | -35.19839 | 2024-11-18 04:12:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 82b24cda-fc76-39dc-b944-6243f73c1609 | -5.95436 | -42.16432 | 2024-11-18 04:12:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f01f1d78-720a-3062-bf42-38ffe8bf1cf8 | -3.39262 | -53.27761 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f46ffb85-734e-3040-a032-877a7425a37d | -3.50294 | -54.04181 | 2024-11-18 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05e50306-78b4-3bff-9e35-ffd9fbf17dae | -3.8821 | -46.65939 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 816a662f-410b-3b8c-95aa-241336fc758a | -4.95148 | -44.50594 | 2024-11-18 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4c580aa-168a-3f42-8c69-6e11fd1ce714 | -3.62813 | -49.19859 | 2024-11-18 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6788d7a8-b2c3-39c0-9aa9-05d3142a226e | -2.99143 | -52.60721 | 2024-11-18 04:12:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b7c4fbb-79b0-3ce1-8cd9-3add1794ad45 | -6.00348 | -46.3989 | 2024-11-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5681ba47-b6f8-3676-9bc4-17631484094f | -3.06055 | -53.28251 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c796eb32-daa3-3623-b213-50c53dae9246 | -3.06728 | -53.27927 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e78bd541-c42b-3377-897c-5bec8b09cb22 | -3.0642 | -53.28407 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2aa4e864-d254-30b6-9692-af6faac1d1c5 | -4.13786 | -46.7107 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8632242-7ff0-361f-8b26-08a85fc42bd7 | -4.26708 | -44.7034 | 2024-11-18 04:12:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44d4ea33-420e-3bd7-a798-118a7f6b633c | -3.73821 | -52.03908 | 2024-11-18 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bba2abf2-e256-38ab-acb5-a38df6b77c0e | -5.33091 | -44.93729 | 2024-11-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9cb527d-7a56-3d74-a68e-24efaa750979 | -6.03087 | -46.45888 | 2024-11-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dd87620-148a-39f8-82f8-5975ebb77342 | -3.05793 | -54.4141 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f12e6e90-e8da-3497-9715-d42155ed07b8 | -3.43381 | -50.80253 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7778c98f-e1fa-387a-a474-7d0a998029ca | -7.53312 | -35.31419 | 2024-11-18 04:12:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5991c53d-eeec-3b21-b321-5a1c89027e09 | -4.49948 | -49.64175 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d9086af-4375-3611-a768-5ed6f3758aa3 | -9.29932 | -46.20945 | 2024-11-18 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcad965c-36db-3b76-8694-11fb1345d854 | -3.47226 | -49.97474 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8a22a59c-ddae-324b-a4f6-b6b366ed9885 | -4.65651 | -44.08527 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afc6139f-588a-366b-8b99-8b059818a84b | -5.30962 | -46.4014 | 2024-11-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62be7701-fdb0-3455-8892-5e96411ea9b2 | -10.37272 | -41.20642 | 2024-11-18 04:12:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4faf8676-ee02-3ad8-b5dc-095862510308 | -3.03942 | -54.406 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c7401953-8b13-34ee-a73f-37bcb6ea6cd6 | -3.09663 | -53.10834 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdbe387e-b3fe-3cf8-9999-dfb664be43c0 | -3.18261 | -53.25291 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1b53438-fca8-33d3-8438-15de6c4732a8 | -6.58242 | -48.03934 | 2024-11-18 04:12:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49cc4cb5-03a1-371c-b7be-f55a8d5270ec | -3.89117 | -46.62754 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d28e3418-3b1f-36ed-9648-20d151f4ea30 | -5.00897 | -46.85955 | 2024-11-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 690f66c8-09b8-3469-b28f-a3e2c5f376df | -4.73015 | -44.43794 | 2024-11-18 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a9ecf97-ff2c-3980-ade9-d026787e7ed9 | -4.71871 | -49.6241 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1f795d4f-8cd1-3dee-8a85-eb1ca8fb2849 | -3.39005 | -53.27214 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36710141-6bcb-397d-9619-816a74f466b1 | -5.18207 | -44.3075 | 2024-11-18 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c60c5013-0b93-30cf-99ef-117c76c410d5 | -6.53143 | -35.19752 | 2024-11-18 04:12:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 4db45342-6457-305e-941f-90e4b207615c | -4.65594 | -44.08886 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ad3cc41-e010-3521-90c5-31b186a4fc76 | -3.43887 | -50.80337 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a85af1fe-7631-3cc0-9d6a-29fc69d7a119 | -3.88584 | -46.63636 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbc962bb-1764-3ec2-8f49-3e97add63681 | -3.89499 | -46.62805 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9639817-6221-3319-a0ab-41c426f9b9f2 | -4.95438 | -49.50771 | 2024-11-18 04:12:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a60223d-9750-3392-aa05-437df3eb91f9 | -7.0631 | -48.35938 | 2024-11-18 04:12:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f0ff47a-c59a-3f90-bb98-5c5cb47cff9f | -4.73073 | -44.43428 | 2024-11-18 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf863be4-51e1-3b95-9979-ebfe7c6def46 | -7.13354 | -46.63786 | 2024-11-18 04:12:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c76ce9fb-5795-3472-bcab-14ddb025a519 | -3.91112 | -46.13749 | 2024-11-18 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11eb83b0-b367-36fe-8f42-e15829b53b9e | -6.98985 | -39.65923 | 2024-11-18 04:12:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 192aabf4-e514-33a0-b1e6-aa720e5c0b8f | -4.69961 | -49.6258 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10c1ea34-490e-39a6-9284-c7883b256a0a | -4.90557 | -44.02864 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9aeff535-24f8-38d6-9486-f925fa667b12 | -9.29868 | -46.21337 | 2024-11-18 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22bcfad7-27ff-3783-a7bd-950130588181 | -3.97931 | -46.70592 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b071f26-b618-32ed-9d19-9771fb8c43af | -3.94568 | -46.71983 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb0c5e93-12a6-311c-9a7e-56647727a516 | -4.29627 | -50.44495 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aede7d5-2fce-3ffe-9ba5-75dee15c4172 | -3.39338 | -53.27299 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2009a75-60f9-3c78-b162-c5eae476b8bc | -4.11041 | -46.10695 | 2024-11-18 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5223ba27-27db-30ec-bce2-073af37cad4d | -3.55 | -54.58152 | 2024-11-18 04:12:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9981ff66-88f8-3a25-ae11-4cd06846cec1 | -6.0028 | -46.40308 | 2024-11-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6965a583-93d6-34ff-9714-ed21df26de5e | -4.13405 | -46.71004 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0779bfd8-c40a-341b-a5c7-9fa4f8f517cf | -3.88964 | -46.63697 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff52d622-25e5-3882-8df8-2526f988e4f7 | -4.35765 | -45.87257 | 2024-11-18 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7430e24a-0476-3c29-a329-32ef81c4555f | -5.26679 | -47.18863 | 2024-11-18 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ef60135-c620-320c-a16a-5149d13b3605 | -3.3358 | -53.35991 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 146310f1-265e-3a8d-b02c-7b12b80839b1 | -6.49096 | -47.49937 | 2024-11-18 04:12:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2dc03bd9-9024-31dd-b392-3a6e28b0611c | -3.6577 | -50.44698 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 751ae47d-2e87-32a4-969e-3424ecb7f942 | -4.27448 | -50.59306 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90d471c7-f53e-3978-8438-43197b65963e | -3.18681 | -53.24264 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4baf6d36-c247-3acc-becd-07e5e65dd023 | -4.11409 | -46.10757 | 2024-11-18 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1109967d-7c1e-364d-8373-874295a54fd4 | -3.38746 | -53.27169 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e972d36-3969-3b53-8433-bbbb6ef90252 | -5.14209 | -47.21483 | 2024-11-18 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45dce40f-a37f-33eb-86a6-5336ac110a0f | -4.90892 | -44.02919 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3adaf626-7cac-3b02-b0f9-35e6020e584c | -3.59199 | -53.78157 | 2024-11-18 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 423cb168-401b-351b-b6b7-009be1fd58ac | -3.43838 | -50.80637 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 058fd194-d25b-30e6-9fd3-3898648405e6 | -3.39816 | -50.73581 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c439ba2-65de-32f8-80e5-1e29bd2723b0 | -3.36963 | -53.31901 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 769f990b-9cc0-3f81-a9d9-f2f4edfc5b69 | -3.52864 | -50.25833 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acbd2590-486a-30f8-aaee-3e3277be0606 | -3.06491 | -53.27974 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47b7a0ac-37d8-3fcc-bd5c-7b28bef8600c | -5.22666 | -48.77277 | 2024-11-18 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1e7cb3e-f060-3fbe-b34c-65b83ea3d7e5 | -5.24496 | -44.75204 | 2024-11-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f9870cb-2f2a-3de9-8c5d-50956aff9b47 | -3.58436 | -53.46006 | 2024-11-18 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 829f674b-899c-3c47-b61a-c56ab10a2953 | -3.37321 | -53.33394 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bcb9b78-43a8-3327-bdd5-184d5e83e07a | -3.06349 | -53.2884 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 35131d7d-70cf-37ea-87a7-5b7321177944 | -3.9442 | -46.70501 | 2024-11-18 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fe07f75-fe4e-3de8-abf0-7da8653628f1 | -3.18786 | -53.25842 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1144afd-5392-397d-8ed0-7a6a1193c694 | -4.74321 | -44.90926 | 2024-11-18 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8aabd4fa-8a6d-344f-86fa-e802ff57d0c7 | -3.58306 | -53.45791 | 2024-11-18 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be8eccb7-d338-3062-9a17-c90ad00198d7 | -4.58865 | -44.22942 | 2024-11-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88d4a632-8fa7-3c61-b3ea-17bf7e6ae910 | -3.05321 | -54.40281 | 2024-11-18 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 77a82952-38ca-3e08-b835-a922df715e93 | -3.66261 | -50.44786 | 2024-11-18 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dcd32823-0a56-3b2e-a5fd-453fd671f5e8 | -4.2767 | -50.58879 | 2024-11-18 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d69c6d25-310b-3439-8be3-0029c4014909 | -6.47882 | -42.3714 | 2024-11-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8ee87926-7f68-37d9-a7c2-4b96a2a71381 | -3.38411 | -53.27099 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef7575ba-42e4-3c57-9ed0-6ae215a2a338 | -6.3768 | -41.54733 | 2024-11-18 04:12:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 33b60fc7-de86-321a-95d6-ce2ba6c015d8 | -3.32495 | -50.49546 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 68949dfb-8b69-3632-b01d-04bf696d91e3 | -3.18543 | -53.23582 | 2024-11-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b26f3fc0-cbbf-3cbe-8a08-dc9e4eb083c7 | -3.33461 | -50.50315 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4576fbda-2640-3e17-b345-24d45b61f374 | -6.49017 | -47.5042 | 2024-11-18 04:12:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47cef5ae-3108-3822-8a51-e9900fa1bf67 | -3.43331 | -50.80555 | 2024-11-18 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d01ba4f-b593-3a6b-bd80-17678b1edc03 | -5.26872 | -47.18611 | 2024-11-18 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README24.md)
