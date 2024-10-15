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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 629e5e4b-bb29-3721-a2df-32588e7b00a1 | -6.94857 | -45.21467 | 2024-10-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aae7fae1-2672-35d1-bfb0-26bb5241971c | -6.94855 | -45.21097 | 2024-10-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3869f149-c8ed-3ec2-bbec-6c87bff61e3f | -6.94797 | -45.21449 | 2024-10-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5be4b9bd-5f0c-30a3-b87e-c84af77edfc2 | -6.94517 | -45.21027 | 2024-10-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80b07b17-dc97-3aab-800c-f9d7f296d4bb | -6.94173 | -44.59381 | 2024-10-15 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c194cf54-4421-37c7-bbf3-aa753bd0efdb | -6.94055 | -44.59634 | 2024-10-15 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54500fff-ca33-3a4f-a509-2c17076d6208 | -6.93785 | -44.5931 | 2024-10-15 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5a53841-68e8-3b2b-9182-cef338b07fbc | -6.90549 | -44.37578 | 2024-10-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5b97cd6f-9d3c-3b9f-8b70-7d530cc0585e | -7.82517 | -43.99427 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f752b7f-07dd-3e18-94c4-75e2a515fda5 | -7.82443 | -43.99866 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d40d8c3-6c7e-3aee-b962-101d8f3853ba | -7.78303 | -43.88982 | 2024-10-15 04:02:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8753dd89-6aaf-3f07-b499-b07a91c9af9f | -7.77788 | -43.8981 | 2024-10-15 04:02:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 557fb213-2c67-3e40-890f-7733a6311a60 | -7.46632 | -44.09305 | 2024-10-15 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1aa2ded4-9fae-3b04-903e-daaaf731c02c | -7.46511 | -44.09479 | 2024-10-15 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3155dd19-f5d4-3366-9738-7b27177e48e0 | -7.46437 | -44.09929 | 2024-10-15 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2168e9fd-d118-3bba-ad52-3f297405f5c6 | -7.46181 | -44.09691 | 2024-10-15 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c49a577b-59e3-30ed-9321-a8f9637c8649 | -7.46062 | -44.09869 | 2024-10-15 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59ae2d1d-762f-3032-8996-087374a4d0b0 | -7.3295 | -44.2814 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 118c33a6-86d5-3441-b2ba-168b5b4b0b9e | -6.68856 | -43.6484 | 2024-10-15 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d2843e9-d1e3-376d-a668-45108589b1d6 | -6.6856 | -43.6434 | 2024-10-15 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d8e193bd-9c67-3e83-8fe7-71f82047fb15 | -6.58292 | -43.95428 | 2024-10-15 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7bb7ae65-959c-34e8-941d-eaa1baa7d711 | -6.67913 | -44.07849 | 2024-10-15 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d5534129-4dcb-3165-afd7-bd1ef930f9d5 | -8.12757 | -43.96493 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f8a7804-503d-3d2b-b863-31c0b6452373 | -6.58463 | -44.17754 | 2024-10-15 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 491e51d6-2658-3f97-ae01-7436b798f7e4 | -6.5815 | -44.17835 | 2024-10-15 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7a909387-de3c-3ddf-aa63-48b9ee06f469 | -6.58084 | -44.17678 | 2024-10-15 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f441063-7f05-3476-aea6-c548f909c4f3 | -6.57972 | -44.23003 | 2024-10-15 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| af4eac74-2317-3aec-8ac4-96db3735720f | -8.94688 | -45.03955 | 2024-10-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22f6207e-5daa-39eb-b822-4cf6923b7769 | -8.91406 | -45.06224 | 2024-10-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ebc8ab29-9662-386f-8a8a-0260f25c76ef | -8.85443 | -44.83862 | 2024-10-15 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70b3f274-3c99-38b6-b47b-51983e274051 | -8.85229 | -44.84067 | 2024-10-15 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce2981ca-efe3-3da5-9614-c73f59e6dd9c | -8.28854 | -44.85042 | 2024-10-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dde90a2-b184-3b45-9e43-3bd6007299c3 | -8.28465 | -44.84981 | 2024-10-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 129f25a4-ff3f-3883-9194-b1816084ee05 | -8.24812 | -44.85371 | 2024-10-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af7f6ce0-6647-37f9-a956-e4684070d2a1 | -8.06501 | -45.38913 | 2024-10-15 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac0141ce-2b6c-30ce-a670-0d4b9945c0ce | -8.03191 | -44.82114 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 860ef238-1765-3d3a-b7a0-48e6e210196f | -8.03109 | -44.826 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4cd5a252-be65-3c06-9aea-413c128e8116 | -8.01568 | -44.79915 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49f62d6d-e85e-3c6d-9072-c27ab15f92d6 | -8.01015 | -44.80814 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3f0c1a08-4b37-3843-aa0e-04062eab7197 | -8.00934 | -44.81293 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 236f7d34-6acf-34cf-badb-23a0873b7056 | -8.00709 | -44.8027 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 478378c2-208f-3311-be0f-1a1c939eb036 | -8.00627 | -44.80753 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81c77f6c-a959-3dad-9946-d08b3f0ae717 | -8.00544 | -44.81235 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b9a53a2-9e21-3778-a409-53b5697f9ded | -8.00464 | -44.81705 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e24ba305-d4fd-3c19-87f9-90b7dc0ec672 | -8.00238 | -44.80692 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5dcbecdf-f952-363f-b856-6c8510db5614 | -8.15198 | -43.9487 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ea5e886-ecbf-3049-ba90-8473631f2866 | -8.14753 | -43.95261 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5bd487a-d7c4-3a7f-bec1-87059282805c | -8.13641 | -43.9572 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48f23749-3036-3b53-a831-eea074fb7d4f | -8.13492 | -43.95988 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e101a0d3-9e5c-3bca-9fc1-773101daafd6 | -8.13199 | -43.96107 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 039dee8a-eeb6-345e-b322-0a715e726479 | -8.13127 | -43.96549 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b628408-5fbe-34db-8b39-7e64f13ded63 | -8.13122 | -43.95936 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44fd22e4-b1a3-3c7a-aac5-fb148067a726 | -8.13047 | -43.96378 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7a9f888-e658-3459-af0f-33034a54cf78 | -8.12829 | -43.96054 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94a32465-0c3d-3b7d-839b-cd0f6d8158e4 | -9.83536 | -45.05672 | 2024-10-15 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f856ada8-0e19-3fc5-81ac-a41fbdaf8226 | -9.83452 | -45.06162 | 2024-10-15 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fee452b0-b9bd-3543-9256-f90046c9dc71 | -9.45981 | -45.50594 | 2024-10-15 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4332a81e-888d-37be-b9de-4e9ce0b4fe52 | -9.45584 | -45.50525 | 2024-10-15 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 729324a2-555a-3da2-8c99-18151aefe177 | -9.45525 | -45.50873 | 2024-10-15 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9653429-b637-3c30-a761-e97483cee3ea | -10.13843 | -44.83131 | 2024-10-15 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0db7ef33-7012-368c-86b0-66deb47fef51 | -10.06763 | -45.04179 | 2024-10-15 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7cb5cd59-092d-3d29-8397-3aa57b4be24a | -10.73958 | -44.69864 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b0de492-423e-389f-8984-d57f756782d5 | -10.49137 | -44.90832 | 2024-10-15 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0642c6c4-808a-3fc9-98c1-d02cca119299 | -10.44846 | -45.02296 | 2024-10-15 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8b4484d-896a-3906-aa93-03083845228c | -10.39231 | -44.82377 | 2024-10-15 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d01dbcb6-8348-38f3-8086-ecafea0cd3b3 | -10.38933 | -44.81848 | 2024-10-15 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| acc6179f-4718-3d03-b28e-7893d7c7fee1 | -10.76113 | -44.8317 | 2024-10-15 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84f2fc09-43b5-3434-a56a-c7b3c88dcd77 | -4.45987 | -45.88696 | 2024-10-15 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7601057-47a7-3fce-9193-7744c3c33967 | -4.71796 | -46.16032 | 2024-10-15 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43d3f5f6-1119-3931-b9f5-e9ff4fc1bbc8 | -4.71725 | -46.16465 | 2024-10-15 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff705e2c-b9a2-3fa4-b84e-2b9678a1a81f | -4.71568 | -46.1629 | 2024-10-15 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 78672616-fd4f-3c76-91de-fab65a9f3c3a | -4.71495 | -46.16721 | 2024-10-15 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d72f2c5e-b9ca-325e-bc81-48595f4b9b67 | -4.7135 | -46.15953 | 2024-10-15 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0b698c42-01d3-3f03-8936-bc74fb1be94c | -4.71278 | -46.16395 | 2024-10-15 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 64ee03b1-0cd4-3cfb-bb9c-746f97f334cc | -4.70904 | -46.15869 | 2024-10-15 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ffc54130-31e2-39a3-8448-bbc36e5369c9 | -4.70831 | -46.16315 | 2024-10-15 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c78ad5c4-3569-3038-9fee-4a3758010eca | -4.70385 | -46.16231 | 2024-10-15 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1f4dbda-b30d-36f1-9d77-ea7027cd0770 | -5.30716 | -45.00211 | 2024-10-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13293b9d-e5d3-3a07-ac56-93b127c2dcaa | -5.48287 | -45.51522 | 2024-10-15 04:02:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 153258b1-6845-3a25-82b2-2f9d7e4efa1e | -5.42405 | -45.47749 | 2024-10-15 04:02:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6dc2c0aa-fce4-302b-970c-70a9a78db0a6 | -5.38573 | -46.1375 | 2024-10-15 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6a9037b-ed7c-366a-b5e2-a966b991046d | -5.29809 | -46.39054 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dee893b-2905-3cb0-b497-44ec3b719354 | -5.2966 | -46.39946 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1223545-3e7b-3d1f-bf51-123646401d06 | -5.29585 | -46.40394 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b9064e2-a365-3974-8a2f-03de231c0e04 | -5.2936 | -46.38974 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01269aeb-cc60-397d-814d-300d12c11c76 | -5.29285 | -46.39425 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e21abcc-461f-3ed0-b30e-b1439b456f40 | -5.2921 | -46.39874 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8ac210e-410f-3e26-8acd-d94e04aff093 | -5.29135 | -46.40321 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d6599d9-e43d-34da-ac75-243c78f2ffa5 | -5.2891 | -46.38901 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0de12650-390f-3ee2-a46b-4342f6f82f2d | -5.28834 | -46.39354 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3badf2f-e074-3550-b3a0-bb7786618a98 | -5.28758 | -46.39804 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f610fe7-3dd1-3c29-a1d8-fd188584f4e8 | -5.28684 | -46.40249 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6faf197c-f71d-3ed0-84ea-009bbe58dc8f | -5.28459 | -46.3883 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7770dd94-9ae9-37bf-9b3a-05845b8d0758 | -5.28383 | -46.39283 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7258f4a-253c-3cd2-bad6-5b42aa2e9d7e | -5.28233 | -46.40175 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfefb61e-bba8-375e-9c77-fd38ca0f53b5 | -5.28231 | -46.37441 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1521268f-8577-3ceb-98a0-d37eaaad4eb8 | -5.28158 | -46.37875 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd0d7b90-bef7-393b-8ed0-6e4c8074a2a8 | -5.28088 | -46.35549 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0938c08-5f4d-3acc-b054-2a8e5b5a8608 | -5.28083 | -46.38314 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a927798-5c25-3e29-936b-58577e006e81 | -5.28012 | -46.35997 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README28.md)
